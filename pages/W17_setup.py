import subprocess
import streamlit as st

st.set_page_config(page_title="W17 driftsättning", layout="wide")


def open_excel_file(file_path):
    try:
        subprocess.call(["open", "-a", "Microsoft Excel", file_path])
    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage
file_path = "files/W17_setup.xlsm"
if st.button("Open Excel File"):
    open_excel_file(file_path)
