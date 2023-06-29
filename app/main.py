from fastapi import FastAPI
import os
import openai
from dotenv import load_dotenv
from pydantic.main import BaseModel

from app import gen_init

app = FastAPI()
app.include_router(gen_init.router)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))

openai.organization = os.getenv("OPENAI_API_ORGANIZATION")
openai.api_key = os.getenv("OPENAI_API_KEY")

class Input(BaseModel):
    data: str

@app.post("/gpt/gen-doc")
def gen_docs(
        input_text: Input
):
    text = """
I'm create an API documentation website, and I'd like you to help me with one of the pages that API documentation

1. Please provide the response content in the "markdown" format, so I can copy and paste it directly. Keep this constraint in mind while writing.
2. Regardless of the language I use, I need the content written in Korean.
3. I will provide some controller layer code written in the Java language, please write me parameter detail and response type and name
4. Class names and objects should never be exposed to the code provided!
5. Wrap the entire response text using <pre> and </pre> tags so I can copy all the content easily.
6. Answer only so that the response starts with <pre> and ends with </pre>
7. Please write an example request and response in json form
8. ```don't start ```markdown please.

Here's an example api code you can refer to:


    """
    text += input_text.data
    response = openai.ChatCompletion.create(
        # engine="text-davinci-003",
        # model="gpt-4",
        model="gpt-3.5-turbo",
        # model='text-davinci-003',
        # prompt=text,
        messages=[{"role": "system", "content": str(text)}],
        # max_tokens=4000,
        # top_p=1,
        # n=1,
        stop=None,
        # temperature=0.5,
        # stop=["\n"]
    )
    # print(response.choices[0].text)
    print("==============")
    output_text = response['choices'][0]['message']['content']
    print(output_text)
    return output_text


@app.post("/gpt/gen_testcode")
def gen_testcode(gen_text: str):

    print("========================")
    print(gen_text)


    text = """
You are Java Backend Developer manager
I'm trying to write a Java unit test code. You make the test code.
I will use java language

1. Use JUnit5
2. Make the method name snake case
3. Comment your test code using the @Display annotation
4. Write comments in Korean using the @Display annotation.
5. Create meticulous test code for all edge cases 
6. Please don't say anything other than test code

Here's an example api code you can refer to:

    """
    text += gen_text

    response = openai.ChatCompletion.create(
        # engine="text-davinci-003",
        # model="gpt-4",
        model="gpt-3.5-turbo",
        # model='text-davinci-003',
        # prompt=text,
        messages=[{"role": "system", "content": str(text)}],
        # max_tokens=4000,
        # top_p=1,
        # n=1,
        stop=None,
        # temperature=0.5,
        # stop=["\n"]
    )
    # print(response.choices[0].text)
    print("==============")
    output_text = response['choices'][0]['message']['content']
    print(output_text)

    return {
        "text_code": text
    }
