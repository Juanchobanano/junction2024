import streamlit as st
import pandas as pd
import numpy as np
import time
import plotly.express as px


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
col0.metric("Pre-production", "✂️")
col1.metric("Average Target Weight (kg)", f"{target_weight:.2f}")
col2.metric("Average Actual Weight (kg)", f"{actual_weight:.2f}", delta=5.6)
col3.metric("Weight Deviation (kg)", f"{weight_deviation:.2f}", delta=-0.5)
col5.success("OK", icon="👍")

col0, col1, col2, col3, col5 = st.columns(5)
col0.metric("Cooking", "🍳")
col1.metric("Average Target Weight (kg)", f"{target_weight:.2f}")
col2.metric("Average Actual Weight (kg)", f"{actual_weight:.2f}", delta=5.6)
col3.metric("Weight Deviation (kg)", f"{weight_deviation:.2f}", delta=-0.5)
col5.success("OK", icon="👍")

col0, col1, col2, col3, col5 = st.columns(5)
col0.metric("Storage", "📥")
col1.metric("Average Target Weight (kg)", f"{target_weight:.2f}")
col2.metric("Average Actual Weight (kg)", f"{actual_weight:.2f}", delta=5.6)
col3.metric("Weight Deviation (kg)", f"{weight_deviation:.2f}", delta=-0.5)
col5.success("OK", icon="👍")

col0, col1, col2, col3, col5 = st.columns(5)
col0.metric("Packing", "📦")
col1.metric("Average Target Weight (kg)", f"{target_weight:.2f}")
col2.metric("Average Actual Weight (kg)", f"{actual_weight:.2f}", delta=5.6)
col3.metric("Weight Deviation (kg)", f"{weight_deviation:.2f}", delta=-0.5)
col5.warning("Discrepancy detected!", icon="⚠️")


# Machine Status Section
st.header("Machine Status Overview 🤖")

# Cooking Machines Status
st.subheader("Cooking Machines 🍳")
cooking_machines_status = {
    "Machine 1": "Running",
    "Machine 2": "Idle",
    "Machine 3": "Maintenance",
}
cooking_status_df = pd.DataFrame(list(cooking_machines_status.items()), columns=["Machine", "Status"])
cooking_status_fig = px.bar(
    cooking_status_df,
    x="Machine",
    y="Status",
    color="Status",
    title="Cooking Machines Status",
    labels={"Status": "Status"},
)
st.plotly_chart(cooking_status_fig, use_container_width=True)

# Cutting Machines Status
st.subheader("Cutting Machines ✂️")
cutting_machines_status = {
    "Machine A": "Running",
    "Machine B": "Idle",
    "Machine C": "Running",
}
cutting_status_df = pd.DataFrame(list(cutting_machines_status.items()), columns=["Machine", "Status"])
cutting_status_fig = px.bar(
    cutting_status_df,
    x="Machine",
    y="Status",
    color="Status",
    title="Cutting Machines Status",
    labels={"Status": "Status"},
)
st.plotly_chart(cutting_status_fig, use_container_width=True)

