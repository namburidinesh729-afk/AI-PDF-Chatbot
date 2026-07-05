

from langchain_core.prompts import ChatPromptTemplate
from core.llm import llm

notes_prompt = ChatPromptTemplate.from_template("""
You are an expert professor.

Read the following study material.

Generate clean study notes.

Requirements:

• Use headings.

• Use bullet points.

• Highlight important concepts.

• Make it easy for exam revision.

Document:
{context}
""")

def generate_notes(context):
    chain = notes_prompt | llm
    response = chain.invoke(
        {
            "context": context
        }
    )
    return response.content