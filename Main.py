import streamlit as st
import pandas as pd
import numpy as np

st.title("EASY REPORT")
st.subheader("An easy way to generate reports")
st.write("Upload your data file (CSV or Excel) to get started.")
uploaded_file = st.file_uploader("Choose a file", type=["csv", "xlsx"])
if uploaded_file is not None:
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.write("Data Preview:")
    st.dataframe(df.head())

    if st.button("Generate Report"):
        st.write("Generating report...")
        report = df.describe(include='all').T
        report['missing_values'] = df.isnull().sum()
        report['missing_percentage'] = (df.isnull().mean() * 100).round(2)
        
        st.write("Report:")
        st.dataframe(report)

        csv = report.to_csv(index=True).encode('utf-8')
        st.download_button(
            label="Download Report as CSV",
            data=csv,
            file_name='data_report.csv',
            mime='text/csv',
        )
else :
    st.info("Please upload a CSV or Excel file to generate a report.")