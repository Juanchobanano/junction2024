import streamlit as st
import pandas as pd
import numpy as np
import time



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


# Mock data generation
def generate_mock_data():
    # Simulating data for weights, sustainability, and gamification scores
    data = {
        "Timestamp": pd.date_range(start="2024-11-01", periods=100, freq="H"),
        "Product_ID": np.random.choice(product_options, 100, replace=True),
        "Target_Weight": np.round(np.random.uniform(200, 220, 100), 2),
        "Actual_Weight": np.round(np.random.uniform(195, 225, 100), 2),
        "Sustainability_Score": np.random.randint(70, 100, 100),
        "Gamification_Points": np.random.randint(0, 100, 100)
    }
    return pd.DataFrame(data)

# Generate mock data
df = generate_mock_data()

# Header
st.header("Factory Management Dashboard 🏭")

product_ids = df["Product_ID"].unique()
selected_product = st.selectbox("Select a product", product_options, index=0)


# Display Production Metrics
target_weight = df["Target_Weight"].mean()
actual_weight = df["Actual_Weight"].mean()
weight_deviation = actual_weight - target_weight

# Displaying Production Metrics
col0, col1, col2, col3, col5 = st.columns(5)
col0.metric("Cooking", "🍳")
col1.metric("Average Target Weight (kg)", f"{target_weight:.2f}")
col2.metric("Average Actual Weight (kg)", f"{actual_weight:.2f}", delta=5.6)
col3.metric("Weight Deviation (kg)", f"{weight_deviation:.2f}", delta=-0.5)
col5.warning("ALERT!")

# Filter data based on the selected product
df_filtered = df[df["Product_ID"] == selected_product]
