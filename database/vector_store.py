
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