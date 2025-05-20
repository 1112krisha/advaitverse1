# modules/visualizations.py
import streamlit as st
import pandas as pd
import plotly.express as px

def run_visualizations():
    st.subheader("📊 Visualization Module")

    csv_file = st.file_uploader("Upload CSV for Visualization", type=["csv"], key="viz_csv")

    if not csv_file:
        return

    df = pd.read_csv(csv_file)
    st.write("📄 Data Preview:")
    st.dataframe(df)

    numeric_cols = df.select_dtypes(include='number').columns.tolist()
    all_cols = df.columns.tolist()

    chart_type = st.selectbox("Select Chart Type", ["Bar", "Line", "Scatter", "Pie"])

    x_col = st.selectbox("Select X-axis", options=all_cols)
    y_col = st.selectbox("Select Y-axis", options=numeric_cols)

    fig = None

    if chart_type == "Bar":
        fig = px.bar(df, x=x_col, y=y_col)
    elif chart_type == "Line":
        fig = px.line(df, x=x_col, y=y_col)
    elif chart_type == "Scatter":
        fig = px.scatter(df, x=x_col, y=y_col)
    elif chart_type == "Pie":
        fig = px.pie(df, names=x_col, values=y_col)

    if fig:
        st.plotly_chart(fig, use_container_width=True)

        # Download HTML version
        st.download_button(
            label="📥 Download Interactive Chart (HTML)",
            data=fig.to_html(),
            file_name="interactive_chart.html",
            mime="text/html"
        )
