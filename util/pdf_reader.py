# utils/pdf_reader.py

import PyPDF2

def extract_text(pdf_file):
    """
    Extracts all text from the uploaded PDF file.

    Args:
        pdf_file: Uploaded file object (from Streamlit uploader)

    Returns:
        text (str): Complete extracted text from PDF
    """
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() + "\n"
    return text
