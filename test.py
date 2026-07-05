# from langchain_huggingface import HuggingFaceEmbedding
# print("Import Successful!")

from sentence_transformers import SentenceTransformer

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

print("Model Loaded Successfully!")