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
summary_prompt = ChatPromptTemplate.from_template("""
You are an expert teacher.
Read the following document carefully.
Generate a well-structured summary in simple English.
Document:
{context}
""")
def generate_summary(context):
    chain = summary_prompt | llm
    response = chain.invoke(
        {
            "context": context
        }
    )
    return response.content