
from langchain_core.prompts import ChatPromptTemplate
from core.llm import llm
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