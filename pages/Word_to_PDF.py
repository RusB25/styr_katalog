import streamlit as st
from docx2pdf import convert
import os
from zipfile import ZipFile


# Function to convert and zip files
def convert_and_zip(files):
    output_dir = "converted_files"
    os.makedirs(output_dir, exist_ok=True)

    for file in files:
        convert(file, output_dir)

    zip_filename = "converted_files.zip"
    with ZipFile(zip_filename, "w") as zipf:
        for root, _, files in os.walk(output_dir):
            for file in files:
                zipf.write(os.path.join(root, file), file)

    return zip_filename


st.title("Word to PDF Converter")

uploaded_files = st.file_uploader(
    "Choose Word files", accept_multiple_files=True, type=["docx"]
)

if uploaded_files:
    if st.button("Convert to PDF"):
        with st.spinner("Converting..."):
            # Save uploaded files to disk
            for uploaded_file in uploaded_files:
                with open(uploaded_file.name, "wb") as f:
                    f.write(uploaded_file.getbuffer())

            # Convert and zip files
            zip_filename = convert_and_zip(
                [uploaded_file.name for uploaded_file in uploaded_files]
            )

            # Provide download link
            with open(zip_filename, "rb") as f:
                st.download_button(
                    "Download Converted Files", f, file_name=zip_filename
                )
