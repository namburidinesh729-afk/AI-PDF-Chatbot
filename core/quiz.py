

from langchain_core.prompts import ChatPromptTemplate
from core.llm import llm

quiz_prompt = ChatPromptTemplate.from_template("""
You are an expert teacher.
Read the following study material.

Generate 10 multiple choice questions.

Each question should have:

Question

A)

B)

C)

D)

Correct Answer

Document:
{context}
""")

def generate_quiz(context):
    chain = quiz_prompt | llm
    response = chain.invoke(
        {
            "context": context
        }
    )
    return response.content