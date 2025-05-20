# modules/statistics.py
import streamlit as st
import pandas as pd

def run_statistics():
    st.subheader("📈 Statistics Module")
    csv_file = st.file_uploader("Upload a CSV file for Statistics", type=["csv"], key="stats_csv")

    if csv_file:
        df = pd.read_csv(csv_file)
        st.write("🔍 Preview of Uploaded Data:")
        st.dataframe(df)

        numeric_cols = df.select_dtypes(include='number').columns.tolist()

        if not numeric_cols:
            st.warning("No numeric columns found for statistical analysis.")
            return

        st.markdown("### 📊 Summary Statistics")
        stats_df = df[numeric_cols].describe().T  # mean, std, min, max, etc.
        stats_df = stats_df.rename(columns={
            "50%": "median"
        })

        st.dataframe(stats_df)

        # Download option
        csv = stats_df.to_csv().encode('utf-8')
        st.download_button(
            label="📥 Download Statistics as CSV",
            data=csv,
            file_name="statistics_summary.csv",
            mime='text/csv',
        )
