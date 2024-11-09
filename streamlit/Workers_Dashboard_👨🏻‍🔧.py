import streamlit as st

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


def create_column(col, product):
    grams_to_change = product['grams_to_change']

    if grams_to_change > 0:
        funny_gif_url = "https://media.tenor.com/CPWZJ9HA3_YAAAAM/justin-timbelake-stare.gif"
        icon_to_show = "⬆️"
        symbol_to_show = "+"
    elif grams_to_change < 0:
        icon_to_show = "⬇️"
        funny_gif_url = "https://media.tenor.com/CPWZJ9HA3_YAAAAM/justin-timbelake-stare.gif"
        symbol_to_show = "-"
    else:
        icon_to_show = "👍"
        funny_gif_url = "https://media.tenor.com/9v5-Fa6QXOAAAAAM/hello-kitty-bow-kitty-bow.gif"
        symbol_to_show = ""

    col.metric("Product", product["name"])
    col.metric("Grams to Change", f"{grams_to_change}g {icon_to_show}", delta=symbol_to_show)
    col.image(funny_gif_url, width=250)


col1, col2, col3 = st.columns(3)
create_column(col1, products[0])
create_column(col2, products[1])
create_column(col3, products[2])