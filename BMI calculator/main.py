import streamlit as st

# Function to calculate BMI
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

# Function to determine BMI category
def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight", "⚠️ You are under the healthy weight range. Please consider gaining weight."
    elif 18.5 <= bmi < 24.9:
        return "Normal weight", "✅ You are within the healthy weight range. Keep it up!"
    elif 25 <= bmi < 29.9:
        return "Overweight", "⚠️ You are slightly above the healthy weight range. Consider a balanced diet."
    else:
        return "Obesity", "❗ You may be at risk for health issues. It's important to consult with a healthcare professional."

# Streamlit UI setup
st.set_page_config(page_title="BMI Calculator", layout="centered", page_icon="⚖️")
st.title("BMI Calculator ⚖️")
st.markdown(
    """
    <style>
    .main {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
    }
    .stTextInput, .stNumberInput, .stButton {
        font-size: 16px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Add introductory text 
st.markdown(
    """
    **Please enter your weight in kilograms and height in meters to calculate your BMI.**
    🏋️‍♂️🧘‍♀️
    """,
    unsafe_allow_html=True,
)

# Input fields for weight and height
weight = st.number_input("Enter your weight (kg) 💪", min_value=1.0, step=0.1, format="%.1f", key="weight")
height = st.number_input("Enter your height (m) 📏", min_value=0.1, step=0.01, format="%.2f", key="height")

# Add some space for UI clarity
st.markdown("<br>", unsafe_allow_html=True)

# Add a button to calculate BMI
if st.button("Calculate BMI 🧮"):
    if weight > 0 and height > 0:
        bmi = calculate_bmi(weight, height)
        category, message = bmi_category(bmi)

        # Displaying the results with style
        st.write(f"### Your BMI is: **{bmi:.2f}**")
        st.write(f"### Category: **{category}**")
        st.write(f"**{message}**")

    else:
        st.error("❌ Please enter valid values for both weight and height.")

# Footer
st.markdown(
    """
    ---
    🖥️ Created ❤️ by **Nimra Ulfat** 👩‍💻
    """,
    unsafe_allow_html=True,
)
