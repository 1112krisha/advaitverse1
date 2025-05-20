# modules/tables.py
import streamlit as st
import pandas as pd
import io

def run_tables():
    st.subheader("📄 Table Viewer")

    csv_file = st.file_uploader("Upload CSV for Table Display", type=["csv", "xlsx"], key="table_csv")

    if not csv_file:
        return

    # Load file
    if csv_file.name.endswith(".csv"):
        df = pd.read_csv(csv_file)
    else:
        df = pd.read_excel(csv_file)

    st.write("🔍 Full Table Preview")
    st.dataframe(df, use_container_width=True)

    # Filter by column value
    filter_col = st.selectbox("Select column to filter", options=df.columns)
    filter_val = st.text_input("Enter value to search")

    if filter_val:
        filtered_df = df[df[filter_col].astype(str).str.contains(filter_val, case=False, na=False)]
        st.write("🔍 Filtered Table")
        st.dataframe(filtered_df, use_container_width=True)
    else:
        filtered_df = df

    # Download buttons
    csv = filtered_df.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Download Filtered CSV", csv, "filtered_table.csv", "text/csv")

    excel_buf = io.BytesIO()
    with pd.ExcelWriter(excel_buf, engine="xlsxwriter") as writer:
        filtered_df.to_excel(writer, index=False, sheet_name="Table")

    st.download_button("📥 Download Excel File", excel_buf.getvalue(), "filtered_table.xlsx", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
