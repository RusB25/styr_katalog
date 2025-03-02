import streamlit as st
import json
import os

from components.Footnote import footnote
from components.Divider import blue_divider

# Set page configuration
st.set_page_config(page_title="Product Catalog", layout="wide")


# Load product data from JSON files
def load_products():
    """Load product data from JSON file with error handling."""
    try:
        with open("data/products.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        st.error("Error loading product data. Please check 'products.json'.")
        return []


# Load products
data = load_products()

# Sidebar Filters
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
            # Add a colored horizontal divider between products
            blue_divider()

footnote()
