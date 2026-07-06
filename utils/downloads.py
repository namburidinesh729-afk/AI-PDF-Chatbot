import streamlit as st

from utils.export_pdf import create_pdf
from utils.export_docx import create_docx


def show_download_buttons(text, filename):
    """
    Display TXT, PDF and DOCX download buttons.

    Parameters
    ----------
    text : str
        Content to download.

    filename : str
        Base filename without extension.
    """

    # TXT
    st.download_button(
        "⬇ Download TXT",
        text,
        f"{filename}.txt",
        mime="text/plain"
    )

    # PDF
    pdf_file = create_pdf(
        text,
        f"{filename}.pdf"
    )

    with open(pdf_file, "rb") as file:
        st.download_button(
            "⬇ Download PDF",
            file,
            f"{filename}.pdf",
            mime="application/pdf"
        )

    # DOCX
    docx_file = create_docx(
        text,
        f"{filename}.docx"
    )

    with open(docx_file, "rb") as file:
        st.download_button(
            "⬇ Download DOCX",
            file,
            f"{filename}.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )