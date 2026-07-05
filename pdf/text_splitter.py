
from langchain_text_splitters import RecursiveCharacterTextSplitter
def split_text(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    chunks = []
    for doc in documents:
        split_chunks = splitter.create_documents(
            [doc["text"]],
            metadatas=[
                {
                    "page": doc["page"]
                }
            ]
        )
        chunks.extend(split_chunks)
    return chunks