
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