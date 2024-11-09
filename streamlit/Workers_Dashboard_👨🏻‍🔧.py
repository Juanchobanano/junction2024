import streamlit as st
import time

# Set page title
st.set_page_config(
    page_title="Real-Time Data Science Dashboard",
    page_icon="🏭",
    layout="wide",
)

# Add a title to the app
st.header("Product Weight Adjustment 👨🏻‍🔧")

# Sample sausage-like product data
products = [
    {"name": "Beef 🐄", "icon": "🐄", "grams_to_change": 0},
    {"name": "Chicken 🐔", "icon": "🐔", "grams_to_change": 5.5},
    {"name": "Pork 🐖", "icon": "🐖", "grams_to_change": -20},
    {"name": "Lamb 🐑", "icon": "🐑", "grams_to_change": 10.5},
    {"name": "Turkey 🦃", "icon": "🦃", "grams_to_change": -12.6}
]

# Dropdown select list for choosing a product (for manual selection, if needed)
product_options = [product['name'] for product in products]
selected_product_name = st.selectbox("Select a product", product_options, index=0)

st.divider()

# Find the selected product's details (either automatic or user-selected)
selected_product = next(
    product
    for product in products if product["name"] == selected_product_name)

# Display selected product information
# st.markdown(f"### **{selected_product['name']} {selected_product['icon']}**")

st.markdown(
        f"""
        <div style="font-size:50px; font-weight:bold; text-align:center;">
            {selected_product['name']} {selected_product['icon']}
        </div>
        """,
        unsafe_allow_html=True
)

# Grams to Increase
grams_to_change = selected_product['grams_to_change']
if grams_to_change == 0:
    st.markdown(
        f"""
        <div style="font-size:50px; font-weight:bold; color:#6c757d; text-align:center;">
            {0}g
        </div>
        """,
        unsafe_allow_html=True
    )
elif grams_to_change > 0:

    st.markdown(
        f"""
        <div style="font-size:50px; font-weight:bold; color:#28a745; text-align:center;">
            {grams_to_change}g ⬆️
        </div>
        """,
        unsafe_allow_html=True
    )
else:
    st.markdown(
        f"""
        <div style="font-size:50px; font-weight:bold; color:#dc3545; text-align:center;">
            {grams_to_change}g ⬇️ 
        </div>
        """,
        unsafe_allow_html=True
    )

# Display the selected face or GIF
all_good = (selected_product['grams_to_change'] == 0)
if all_good:
    # Replace with a funny GIF URL (use any GIF URL that suits your needs)
    #funny_gif_url = "./assets/thumbs-up-approve.gif"
    funny_gif_url = "https://media.tenor.com/9v5-Fa6QXOAAAAAM/hello-kitty-bow-kitty-bow.gif"
    col1, col2, col3, col4 = st.columns(4)
    with col3:
        st.image(funny_gif_url, width=400)
else:
    #funny_gif_url = "./assets/justin-timbelake-stare.gif"
    funny_gif_url = "https://media.tenor.com/CPWZJ9HA3_YAAAAM/justin-timbelake-stare.gif"
    col1, col2, col3, col4 = st.columns(4)
    with col3:
        st.image(funny_gif_url, width=300)
