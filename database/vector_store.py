# from langchain_google_genai import GoogleGenerativeAIEmbeddings
# from langchain_community.vectorstores import FAISS
# from dotenv import load_dotenv
# import os
# load_dotenv()
# embeddings = GoogleGenerativeAIEmbeddings(
#     model="gemini-embedding-2-preview",
#     google_api_key=os.getenv("GOOGLE_API_KEY")
# )
# def create_vector_store(chunks):
#     vector_store = FAISS.from_texts(
#         texts=chunks,
#         embedding=embeddings
#     )
#     vector_store.save_local("faiss_index")
#     return vector_store


# from langchain_huggingface import HuggingFaceEmbeddings
# from langchain_community.vectorstores import FAISS
# embeddings = HuggingFaceEmbeddings(
#     model_name="sentence-transformers/all-MiniLM-L6-v2"
# )
# def create_vector_store(chunks):
#     vector_store = FAISS.from_texts(
#         texts=chunks,
#         embedding=embeddings
#     )
#     vector_store.save_local("faiss_index")
#     return vector_store


# from langchain_huggingface import HuggingFaceEmbeddings
# from langchain_community.vectorstores import FAISS
# embeddings = HuggingFaceEmbeddings(
#     model_name="sentence-transformers/all-MiniLM-L6-v2"
# )
# def create_vector_store(chunks):
#     vector_store = FAISS.from_texts(
#         texts=chunks,
#         embedding=embeddings
#     )
#     vector_store.save_local("faiss_index")
# def load_vector_store():
#     return FAISS.load_local(
#         "faiss_index",
#         embeddings,
#         allow_dangerous_deserialization=True
#     )

from functools import lru_cache
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
def create_vector_store(documents):
    vector_store = FAISS.from_documents(
        documents,
        embeddings
    )
    vector_store.save_local("faiss_index")
@lru_cache(maxsize=1)
def load_vector_store():
    return FAISS.load_local(
        "faiss_index",
        embeddings,
        allow_dangerous_deserialization=True
    )