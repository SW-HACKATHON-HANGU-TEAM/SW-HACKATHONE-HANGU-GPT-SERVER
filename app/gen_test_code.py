# import os
# from fastapi import APIRouter
# import openai
# from dotenv import load_dotenv
# from pydantic.main import BaseModel
#
# router = APIRouter()
#
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# load_dotenv(os.path.join(BASE_DIR, ".env"))
#
# openai.organization = os.getenv("OPENAI_API_ORGANIZATION")
# openai.api_key = os.getenv("OPENAI_API_KEY")
#
# class Gpt(BaseModel):
#     text: str
#
#
# @router.post("/gpt/gen_testcode")
# def gen_testcode(gen_text: str):
#     text = """
# I'm trying to write a Java unit test code. You make the test code.
# I will use java language
# 1. Use JUnit5
# 2. Make the method name snake case
# 3. Comment your test code using the @Display annotation
# 4. Write comments in Korean using the @Display annotation.
# 5. Create meticulous test code for all edge cases
# 6. Please don't say anything other than test code
#
# Here's an example api code you can refer to:
#
# package cbnu.io.cbnuswalrami.business.core.domon.post.values;
#
# import cbnu.io.cbnuswalrami.business.core.error.ErrorField;
#
# import javax.persistence.Embeddable;
# import java.util.Objects;
#
# @Embeddable
# public class Description {
#
#     private String description;
#
#     protected Description() {
#
#     }
#
#     private Description(String description) {
#         validateDescription(description);
#         this.description = description;
#     }
#
#     private void validateDescription(String description) {
#         if (description == null || description.isBlank()) {
#             throw new IllegalArgumentException("글을 작성해주세요.", ErrorField.of("description", description));
#         }
#         if (description.length() > 3000) {
#             throw new IllegalArgumentException("게시글을 3000자 이상 넘기지 말아주세요.", ErrorField.of("description", description));
#         }
#     }
#
#     public static Description from(String description) {
#         return new Description(description);
#     }
#
#     @Override
#     public boolean equals(Object o) {
#         if (this == o) return true;
#         if (!(o instanceof Description that)) return false;
#         return Objects.equals(description, that.description);
#     }
#
#     @Override
#     public int hashCode() {
#         return Objects.hash(description);
#     }
#
#     public String getDescription() {
#         return description;
#     }
#
#     @Override
#     public String toString() {
#         return description;
#     }
# }
#
#
#     """
#     text += gen_text
#
#     response = openai.ChatCompletion.create(
#         # engine="text-davinci-003",
#         # model="gpt-4",
#         model="gpt-3.5-turbo",
#         # model='text-davinci-003',
#         # prompt=text,
#         messages=[{"role": "user", "content": str(gen_text)}],
#         # max_tokens=4000,
#         # top_p=1,
#         # n=1,
#         stop=None,
#         # temperature=0.5,
#         # stop=["\n"]
#     )
#     # print(response.choices[0].text)
#     print("==============")
#     output_text = response['choices'][0]['message']['content']
#     print(output_text)
#
#     return {
#         "text_code": text
#     }
