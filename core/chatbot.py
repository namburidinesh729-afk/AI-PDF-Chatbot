
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
load_dotenv()
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0,
    groq_api_key=os.getenv("GROQ_API_KEY")
)
prompt = ChatPromptTemplate.from_template("""
You are a helpful AI Study Assistant.
Use the conversation history when it helps answer follow-up questions.
Answer ONLY using the provided PDF context.
If the answer is not present in the context, reply exactly:
"I couldn't find that information in the uploaded PDF."
Conversation History:
{history}
Context:
{context}
Current Question:
{question}
""")
def ask_groq(context, question, history):
    chain = prompt | llm
    response = chain.invoke(
        {
            "context": context,
            "question": question,
            "history": history
        }
    )
    return response.content