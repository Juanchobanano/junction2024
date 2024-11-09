import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Set page title
st.set_page_config(page_title="Simple Dashboard")

# Add a title to the app
st.title("Simple Dashboard")

# Add a description
st.write("This is a basic dashboard built with Streamlit.")

# Sidebar for user input
st.sidebar.header("User Inputs")

# Slider to adjust a parameter
param = st.sidebar.slider("Select a value", min_value=1, max_value=10, value=5)

# Button to trigger an action
if st.sidebar.button("Generate Plot"):
    # Generate a plot based on the selected parameter
    x = np.linspace(0, 10, 100)
    y = np.sin(x * param)

    # Create the plot
    fig, ax = plt.subplots()
    ax.plot(x, y, label=f"sin(x * {param})")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_title("Sine Wave Plot")
    ax.legend()

    # Display the plot
    st.pyplot(fig)

# Add some more information to the main page
st.subheader("Dashboard Information")
st.write("You can adjust the parameter using the slider in the sidebar. The plot will update when you click the 'Generate Plot' button.")

# Display some sample data
data = {
    "Category": ["A", "B", "C", "D", "E"],
    "Values": [10, 20, 15, 25, 30]
}

st.subheader("Sample Data")
st.write(data)

# Display a bar chart
fig, ax = plt.subplots()
ax.bar(data["Category"], data["Values"])
ax.set_xlabel("Category")
ax.set_ylabel("Values")
ax.set_title("Category vs Values")
st.pyplot(fig)
