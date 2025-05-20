# app.py
import streamlit as st
from utils.pdf_reader import extract_text
from utils.module_parser import detect_modules

st.set_page_config(page_title="Advaitverse", layout="wide")

st.markdown("<h1 style='color:#0077B6;'>Advaitverse</h1>", unsafe_allow_html=True)
st.markdown("### Upload a PDF containing your project details")

pdf_file = st.file_uploader("Upload PDF", type="pdf")

if pdf_file:
    with st.spinner("Reading PDF..."):
        text = extract_text(pdf_file)
        st.success("PDF loaded!")
        st.text_area("PDF Content", text, height=300)

        modules_found = detect_modules(text)
        st.info(f"📦 Modules Detected: {', '.join(modules_found)}")

        if "statistics" in modules_found:
            from modules.statistics import run_statistics
            run_statistics()

        if "visualizations" in modules_found:
            from modules.visualizations import run_visualizations
            run_visualizations()

        if "venn" in modules_found:
            from modules.venn_module import run_venn
            run_venn()
