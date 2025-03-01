import streamlit as st
import json
import os


# Load product data from JSON files
def load_products():
    """Load product data from JSON file with error handling."""
    try:
        with open("data/products.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        st.error("Error loading product data. Please check 'products.json'.")
        return []


# Set page configuration
st.set_page_config(page_title="Product Catalog", layout="wide")

# Load products
data = load_products()

# Sidebar Filters
st.sidebar.markdown(
    """
    <style>
        .sidebar .sidebar-content {
            background-color: #f0f2f6;
        }
    </style>
    """,
    unsafe_allow_html=True,
)
st.sidebar.title("Filter Products")
group_filter = st.sidebar.selectbox(
    "Filter by Group", ["All"] + sorted(set(p["group"] for p in data))
)
search_filter = st.sidebar.text_input("Search Product")

# Filter products
filtered_products = [
    p
    for p in data
    if (group_filter == "All" or p["group"] == group_filter)
    and search_filter.lower() in p["name"].lower()
]

# Group products by their 'group' attribute
grouped_products = {}
for product in filtered_products:
    group = product["group"]
    if group not in grouped_products:
        grouped_products[group] = []
    grouped_products[group].append(product)

# Display products under their respective groups
st.title("Product Catalog")
for group, products in grouped_products.items():
    with st.expander(group, expanded=False):
        for product in products:
            st.markdown(
                f"<h3 style='color: #2196F3;'>{product['name']}</h3>",
                unsafe_allow_html=True,
            )
            col1, col2 = st.columns([1, 2])
            with col1:
                st.image(product["image"], use_container_width=True)
            with col2:
                st.markdown(f"{product['description']}")
                if "login" in product:
                    st.markdown(f"**Login:** {product['login']}")
                if "password" in product:
                    st.markdown(f"**Password:** {product['password']}")
                if "ip_address" in product:
                    st.markdown(f"**Default IP Address:** {product['ip_address']}")
                if "file" in product:
                    try:
                        with open(product["file"], "rb") as file:
                            file_data = file.read()
                        st.download_button(
                            "Download File",
                            data=file_data,
                            file_name=os.path.basename(product["file"]),
                            mime="application/pdf",
                        )
                    except FileNotFoundError:
                        st.error(f"File {product['file']} not found.")
                if "link" in product:
                    st.markdown(f"[Läs mer]({product['link']})")
            st.markdown(
                "<hr style='border: 1px solid #2196F3;'>", unsafe_allow_html=True
            )  # Add a colored horizontal divider between products

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
