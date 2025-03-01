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

# Add author information and bug report link at the bottom
st.markdown(
    """
    <style>
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: #f1f1f1;
            text-align: center;
            padding: 10px;
            font-size: 14px;
            color: #333;
            z-index: 1000;
        }
    </style>
    <div class="footer">
        Created by Ruslan Bagirov © 2025 | <a href="mailto:ruslan861125@gmail.com?subject=Bug Report">Report a Bug</a>
    </div>
    """,
    unsafe_allow_html=True,
)
