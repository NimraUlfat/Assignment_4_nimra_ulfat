import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set up the title and emojis
st.title("📊 Simple Data Dashboard 📊")

# File upload functionality
uploaded_file = st.file_uploader("📂 Choose a CSV file to upload", type="csv")

if uploaded_file is not None:
    # Try to read the CSV file
    try:
        df = pd.read_csv(uploaded_file)
    except Exception as e:
        st.error(f"❌ Error reading the file: {e}")
    
    # Display a preview of the data
    st.subheader("👀 Data Preview")
    st.write(df.head())
    
    # Show data summary (statistics)
    st.subheader("📋 Data Summary")
    st.write(df.describe())
    
    # Filter data based on selected column and value
    st.subheader("🔍 Filter Data")
    columns = df.columns.tolist()
    selected_column = st.selectbox("📝 Select column to filter by", columns)
    unique_values = df[selected_column].unique()
    selected_value = st.selectbox("🔢 Select value", unique_values)

    filtered_df = df[df[selected_column] == selected_value]
    st.write(f"📉 Filtered Data: {selected_column} = {selected_value}")
    st.write(filtered_df)
    
    # Plot the filtered data
    st.subheader("📈 Plot Data")
    x_column = st.selectbox("📊 Select x-axis column", columns)
    y_column = st.selectbox("📊 Select y-axis column", columns)

    if st.button("🔵 Generate Plot"):
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(filtered_df[x_column], filtered_df[y_column], marker='o', linestyle='-', color='b')
        ax.set_xlabel(x_column)
        ax.set_ylabel(y_column)
        ax.set_title(f"📊 Plot of {y_column} vs {x_column}")
        st.pyplot(fig)

else:
    st.write("⏳ Waiting on file upload... Please upload a CSV file to get started.")
