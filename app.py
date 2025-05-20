import streamlit as st
from utils.pdf_reader import extract_text

st.set_page_config(page_title="Advaitverse", page_icon="🔬", layout="wide")

# Sidebar logo
st.sidebar.image("Advait Logo.png", use_container_width=True)

st.title("🔬 Advaitverse – Intelligent Web Generator")
st.markdown("Upload a PDF and generate a smart web application prototype from it.")

# File uploader
uploaded_file = st.file_uploader("📄 Upload a PDF file", type="pdf")

if uploaded_file:
    with st.spinner("Reading PDF..."):
        raw_text = extract_text(uploaded_file)

    st.success("PDF processed successfully.")
    st.subheader("📄 Extracted Text Preview")
    st.write(raw_text[:1000] + "...")  # Preview first 1000 characters

    # In future: Add modules to auto-generate code/UI/statistics from this
else:
    st.info("Please upload a PDF to get started.")
