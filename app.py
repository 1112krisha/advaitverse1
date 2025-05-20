# app.py

import streamlit as st
from utils.pdf_reader import extract_text
from utils.module_parser import detect_modules

# ---------------- UI Setup ----------------
st.set_page_config(page_title="Advaitverse", layout="wide")

st.markdown(
    "<h1 style='text-align:center; color:#0077B6;'>🌐 Advaitverse</h1>",
    unsafe_allow_html=True
)

st.sidebar.image("assets/logo.png", use_column_width=True)  # optional logo
st.sidebar.markdown("## 📂 Navigation")

# Sidebar navigation
menu = st.sidebar.radio("Go to", ["Home", "PDF Upload", "Statistics", "Visualizations", "Venn Diagram", "Tables"])

# ---------------- Routing Logic ----------------
if menu == "Home":
    st.markdown("""
        <div style='color:#023E8A; font-size:18px;'>
        Welcome to <b>Advaitverse</b> — your AI-powered diagnostic assistant.<br>
        Upload a PDF with analysis instructions and let the system auto-build modules like statistics, plots, venn diagrams, and more.
        </div>
    """, unsafe_allow_html=True)

elif menu == "PDF Upload":
    st.markdown("### 📄 Upload PDF with Instructions")
    pdf_file = st.file_uploader("Upload PDF", type="pdf")

    if pdf_file:
        text = extract_text(pdf_file)
        st.success("PDF loaded successfully!")
        st.text_area("📑 PDF Content", text, height=300)

        modules_found = detect_modules(text)
        st.info(f"🧠 Modules Detected: {', '.join(modules_found)}")

        if "statistics" in modules_found:
            from modules.statistics import run_statistics
            run_statistics()

        if "visualizations" in modules_found:
            from modules.visualizations import run_visualizations
            run_visualizations()

        if "venn" in modules_found:
            from modules.venn_module import run_venn
            run_venn()

        if "tables" in modules_found:
            from modules.tables import run_tables
            run_tables()

elif menu == "Statistics":
    from modules.statistics import run_statistics
    run_statistics()

elif menu == "Visualizations":
    from modules.visualizations import run_visualizations
    run_visualizations()

elif menu == "Venn Diagram":
    from modules.venn_module import run_venn
    run_venn()

elif menu == "Tables":
    from modules.tables import run_tables
    run_tables()
