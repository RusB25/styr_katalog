import streamlit as st


# Title of the app
def add_styles():
    st.markdown(
        """
    <style>
    .section-title {
        background-color: #2196F3;
        color: white;
        padding: 10px;
        border-radius: 5px;
    }
    .markdown-section {
        border: 1px solid #ddd;
        padding: 10px;
        border-radius: 5px; 
    }
    </style>
    """,
        unsafe_allow_html=True,
    )
