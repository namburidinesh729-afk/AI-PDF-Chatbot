

from langchain_core.prompts import ChatPromptTemplate
from core.llm import llm

interview_prompt = ChatPromptTemplate.from_template("""
You are a senior technical interviewer.

Read the following study material.

Generate the 15 most important interview questions.

Do not provide answers.

Document:
{context}
""")

def generate_interview_questions(context):
    chain = interview_prompt | llm
    response = chain.invoke(
        {
            "context": context
        }
    )
    return response.content