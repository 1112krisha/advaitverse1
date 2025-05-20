# app.py
import streamlit as st
from utils.pdf_reader import extract_text

st.set_page_config(page_title="Advaitverse", layout="wide")

st.markdown("<h1 style='color:#0077B6;'>Advaitverse</h1>", unsafe_allow_html=True)
st.markdown("### Upload a PDF containing your project details")

pdf_file = st.file_uploader("Upload PDF", type="pdf")

if pdf_file:
    with st.spinner("Reading PDF..."):
        text = extract_text(pdf_file)
        st.success("PDF loaded!")
        st.text_area("PDF Content", text, height=300)
