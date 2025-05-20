import streamlit as st
import PyPDF2
import io
import re

# Page settings
st.set_page_config(page_title="Advaitverse – Intelligent Web Generator", layout="wide")

# Title
st.markdown("""
    <h1 style='text-align: center;'>🧠 Advaitverse – Intelligent Web Generator</h1>
    <p style='text-align: center;'>Upload a PDF and generate a smart web application prototype from it.</p>
""", unsafe_allow_html=True)

# File uploader
uploaded_file = st.file_uploader("📁 Upload a PDF file", type=["pdf"])

if uploaded_file:
    try:
        # Read PDF
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        full_text = ""
        for page in pdf_reader.pages:
            text = page.extract_text()
            if text:
                full_text += text + "\n"

        # Confirm success
        st.success("✅ PDF processed successfully.")

        # Show raw text preview
        with st.expander("📝 Extracted Text Preview"):
            st.write(full_text)

        # Try to split into sections (very basic)
        section_headers = re.findall(r'(\d+\.\s+[A-Z ]+)', full_text)
        sections = re.split(r'\n\d+\.\s+[A-Z ]+', full_text)

        if len(sections) > 1:
            st.markdown("---")
            st.subheader("📂 Auto-generated Sections")

            for idx, content in enumerate(sections[1:]):
                section_title = section_headers[idx] if idx < len(section_headers) else f"Section {idx+1}"
                with st.expander(f"📄 {section_title.strip()}"):
                    st.markdown(content.strip())
        else:
            st.warning("⚠️ Couldn't find clear section splits. Please check your PDF formatting.")

    except Exception as e:
        st.error(f"❌ Error reading PDF: {e}")
else:
    st.info("👆 Upload a PDF file to begin.")
