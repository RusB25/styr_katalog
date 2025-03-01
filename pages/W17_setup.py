import streamlit as st

st.set_page_config(page_title="W17 driftsättning", layout="wide")

filepath = "files/W17_setup.xlsm"
with open(filepath, "rb") as file:
    st.download_button(
        "Download File",
        data=file,
        mime="application/vnd.ms-excel.sheet.macroEnabled.12",
        file_name="W17_setup.xlsm",
    )
