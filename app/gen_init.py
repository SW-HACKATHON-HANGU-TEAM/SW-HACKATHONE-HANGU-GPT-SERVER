import openai
from fastapi import APIRouter

router = APIRouter()
@router.post("/gen-init")
def gen_init(
        project_name: str,
        developer_type: str
):
    text = """
Given the name of a development project, I would like to help you design the process of developing that project. and I want the design to fit the project name and project developer. 

Here's what I'd like help writing:

1. When a project name is given, the items to be designed are as follows. 
 (1) DB design using mermaid code. 
 (2) Description of the DB. The DB description is based on the mermaid code designed above.
 (3) mermaid code mindmap in graph LR format for  development process description
 (4) Development process description

Divided with '(splitPoint)' mark above the number so that each number item can be seen separately.

2. PLEASE provide the response content in the "Markdown" format, so I can copy and paste it directly. Keep this constraint in mind while writing. Don't use html.
3. Regardless of the language I use, I need the content written in Korean.
4. Wrap the entire response text using <pre> and </pre> tags so I can copy all the content easily.
5. Answer only so that the response starts with <pre> and ends with </pre>
6. Make the design difficulty different according to the person who develops it. I will also refer to this

Here's an example project name and developer type you can refer to:
    """
    text += project_name + ',' + developer_type

    response = openai.ChatCompletion.create(
        # engine="text-davinci-003",
        # model="gpt-4",
        model="gpt-3.5-turbo",
        # model='text-davinci-003',
        # prompt=text,
        messages=[{"role": "user", "content": str(text)}],
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
