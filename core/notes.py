import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
load_dotenv()
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)
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