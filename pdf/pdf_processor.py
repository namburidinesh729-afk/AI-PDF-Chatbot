# import os
# from utils import read_pdf
# from text_splitter import split_text
# from vector_store import create_vector_store
# UPLOAD_FOLDER = "pdfs"
# def process_uploaded_pdf(uploaded_file):
#     if not os.path.exists(UPLOAD_FOLDER):
#         os.makedirs(UPLOAD_FOLDER)
#     file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)
#     with open(file_path, "wb") as f:
#         f.write(uploaded_file.getbuffer())
#     text = read_pdf(file_path)
#     chunks = split_text(text)
#     create_vector_store(chunks)
#     return True

import os
from pdf.utils import read_pdf
from pdf.text_splitter import split_text
from database.vector_store import create_vector_store
UPLOAD_FOLDER = "pdfs"
def process_uploaded_pdf(uploaded_file):
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    file_path = os.path.join(
        UPLOAD_FOLDER,
        uploaded_file.name
    )
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    documents = read_pdf(file_path)
    chunks = split_text(documents)
    create_vector_store(chunks)
    return True