import streamlit as st
from utils.pdf_reader import extract_text

# Page config
st.set_page_config(
    page_title="Advaitverse – Intelligent Web Generator",
    layout="wide",
    page_icon="🧠"
)

# Title
st.title("🧠 Advaitverse – Intelligent Web Generator")
st.markdown("Upload a PDF and generate a smart web application prototype from it.")

# File uploader
uploaded_file = st.file_uploader("📂 Upload a PDF file", type=["pdf"])

# Handle uploaded file
if uploaded_file is not None:
    with st.spinner("Processing..."):
        raw_text = extract_text(uploaded_file)

        if raw_text.strip():  # Check if anything was extracted
            st.success("PDF processed successfully.")
            st.subheader("📄 Extracted Text Preview")
            st.write(raw_text)  # Shows full content more reliably than st.text()
        else:
            st.error("❌ No text could be extracted. Please check the PDF content.")
