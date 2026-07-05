# import os
# from dotenv import load_dotenv
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_core.prompts import ChatPromptTemplate
# load_dotenv()
# llm = ChatGoogleGenerativeAI(
#     model="gemini-2.0-flash",
#     temperature=0,
#     google_api_key=os.getenv("GOOGLE_API_KEY")
# )
# flash_prompt = ChatPromptTemplate.from_template("""
# You are an expert teacher.
# Read the following study material.
# Generate 15 flashcards.
# Each flashcard should contain:
# Front:
# <Question>
# Back:
# <Answer>
# Document:
# {context}
# """)
# def generate_flashcards(context):
#     chain = flash_prompt | llm
#     response = chain.invoke(
#         {
#             "context": context
#         }
#     )
#     return response.content

from langchain_core.prompts import ChatPromptTemplate
from core.llm import llm

flash_prompt = ChatPromptTemplate.from_template("""
You are an expert teacher.

Read the following study material.

Generate 15 flashcards.

Each flashcard should contain:

Front:
<Question>

Back:
<Answer>

Document:
{context}
""")

def generate_flashcards(context):
    chain = flash_prompt | llm
    response = chain.invoke(
        {
            "context": context
        }
    )
    return response.content