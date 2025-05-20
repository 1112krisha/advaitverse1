import streamlit as st
import pandas as pd

def run_smart_form(pdf_text=None):
    st.subheader("📝 Smart Form Generator")

    if pdf_text is None:
        st.info("Upload a PDF with form instructions in the PDF Upload section first.")
        return

    st.markdown("### Form generated from PDF instructions:")

    # Example: For demo, we extract dummy fields based on keywords
    # (In real AI-powered app, NLP would parse more intelligently)
    
    # Simple mockup: look for keywords to generate fields
    fields = []
    if "patient name" in pdf_text.lower():
        fields.append({"label": "Patient Name", "type": "text"})
    if "age" in pdf_text.lower():
        fields.append({"label": "Age", "type": "number"})
    if "gender" in pdf_text.lower():
        fields.append({"label": "Gender", "type": "select", "options": ["Male", "Female", "Other"]})
    if "symptoms" in pdf_text.lower():
        fields.append({"label": "Symptoms", "type": "text_area"})

    if not fields:
        st.warning("No recognizable form fields found in the PDF text.")
        return

    form_data = {}
    with st.form("dynamic_form"):
        for field in fields:
            label = field["label"]
            ftype = field["type"]

            if ftype == "text":
                form_data[label] = st.text_input(label)
            elif ftype == "number":
                form_data[label] = st.number_input(label, min_value=0, max_value=150, step=1)
            elif ftype == "select":
                form_data[label] = st.selectbox(label, options=field["options"])
            elif ftype == "text_area":
                form_data[label] = st.text_area(label)
        
        submitted = st.form_submit_button("Submit")

    if submitted:
        st.success("Form submitted successfully!")
        df = pd.DataFrame([form_data])
        st.write("### Entered Data:")
        st.dataframe(df)

        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Download Form Data as CSV", csv, "form_data.csv", "text/csv")
