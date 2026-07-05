
from PyPDF2 import PdfReader
def read_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    documents = []
    for page_number, page in enumerate(reader.pages):
        text = page.extract_text()
        if text:
            documents.append(
                {
                    "text": text,
                    "page": page_number + 1
                }
            )
    return documents