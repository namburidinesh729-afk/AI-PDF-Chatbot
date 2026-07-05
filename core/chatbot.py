# import os
# from dotenv import load_dotenv
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_core.prompts import ChatPromptTemplate
# load_dotenv()
# llm = ChatGoogleGenerativeAI(
#     model="gemini-2.5-flash",
#     temperature=0,
#     google_api_key=os.getenv("GOOGLE_API_KEY")
# )
# prompt = ChatPromptTemplate.from_template(
# """
# You are a helpful AI assistant.
# Answer the user's question ONLY using the context below.
# If the answer is not available in the context,
# say:
# "I couldn't find that information in the uploaded PDF."
# Context:
# {context}
# Question:
# {question}
# """
# )
# def ask_gemini(context, question):
#     chain = prompt | llm
#     response = chain.invoke({
#         "context": context,
#         "question": question
#     })
#     return response.content

# import os
# from dotenv import load_dotenv
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_core.prompts import ChatPromptTemplate
# load_dotenv()
# llm = ChatGoogleGenerativeAI(
#     model="gemini-2.5-flash",
#     temperature=0,
#     google_api_key=os.getenv("GOOGLE_API_KEY")
# )
# prompt = ChatPromptTemplate.from_template("""
# You are a helpful AI assistant.
# Answer ONLY using the provided context.
# If the answer is not found in the context, reply:
# "I couldn't find that information in the uploaded PDF."
# Context:
# {context}
# Question:
# {question}
# """)
# def ask_gemini(context, question):
#     chain = prompt | llm
#     response = chain.invoke({
#         "context": context,
#         "question": question
#     })
#     return response.content

# import os
# from dotenv import load_dotenv
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_core.prompts import ChatPromptTemplate
# load_dotenv()
# import streamlit as st
# st.write("API Key starts with:", os.getenv("GOOGLE_API_KEY")[:8])
# llm = ChatGoogleGenerativeAI(
#     model="gemini-2.0-flash",
#     temperature=0,
#     google_api_key=os.getenv("GOOGLE_API_KEY")
# )
# prompt = ChatPromptTemplate.from_template("""
# You are a helpful AI assistant.
# Answer ONLY using the provided context.
# If the answer is not present in the context, reply:
# "I couldn't find that information in the uploaded PDF."
# Context:
# {context}
# Question:
# {question}
# """)
# def ask_gemini(context, question):
#     chain = prompt | llm
#     response = chain.invoke(
#         {
#             "context": context,
#             "question": question
#         }
#     )
#     return response.content

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
You are a helpful AI assistant.
Answer ONLY using the provided context.
If the answer is not present in the context, reply:
"I couldn't find that information in the uploaded PDF."
Context:
{context}
Question:
{question}
""")
def ask_groq(context, question):
    chain = prompt | llm
    response = chain.invoke(
        {
            "context": context,
            "question": question
        }
    )
    return response.content