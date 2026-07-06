from PyPDF2 import PdfReader
import os

def read_pdf(pdf_path):
    reader = PdfReader(pdf_path)

    documents = []

    filename = os.path.basename(pdf_path)

    for page_number, page in enumerate(reader.pages):
        text = page.extract_text()

        if text:
            documents.append(
                {
                    "text": text,
                    "page": page_number + 1,
                    "source": filename
                }
            )

    return documents