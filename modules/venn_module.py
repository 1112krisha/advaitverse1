# modules/venn_module.py
import streamlit as st
import matplotlib.pyplot as plt
from matplotlib_venn import venn2, venn3
import io

def run_venn():
    st.subheader("🔵 Venn Diagram Module")

    st.markdown("Enter up to 3 comma-separated sets")

    set1 = st.text_input("Set A (e.g. apple, banana, mango)")
    set2 = st.text_input("Set B (e.g. banana, mango, cherry)")
    set3 = st.text_input("Set C (optional)", "")

    if st.button("Generate Venn Diagram"):
        try:
            s1 = set([i.strip() for i in set1.split(",") if i.strip()])
            s2 = set([i.strip() for i in set2.split(",") if i.strip()])
            s3 = set([i.strip() for i in set3.split(",") if i.strip()]) if set3 else None

            fig, ax = plt.subplots()

            if s3:
                venn3([s1, s2, s3], set_labels=("A", "B", "C"))
            else:
                venn2([s1, s2], set_labels=("A", "B"))

            st.pyplot(fig)

            # Downloadable Image
            buf = io.BytesIO()
            fig.savefig(buf, format="png")
            st.download_button(
                label="📥 Download Venn Diagram",
                data=buf.getvalue(),
                file_name="venn_diagram.png",
                mime="image/png"
            )

        except Exception as e:
            st.error(f"Error generating Venn Diagram: {e}")
