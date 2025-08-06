import streamlit as st

# Page configuration
st.set_page_config(page_title="BMI & Health Advisor", page_icon="⚖️", layout="centered")

# Custom CSS styling for better appearance
st.markdown("""
    <style>
        .main {
            background-color: #f0f4f7;
        }
        .stButton button {
            background-color: #4CAF50;
            color: white;
            font-weight: bold;
            padding: 0.6em 1em;
            border-radius: 8px;
        }
        .stButton button:hover {
            background-color: #45a049;
        }
        .title {
            font-size: 36px;
            color: #333;
            text-align: center;
        }
        .subtitle {
            font-size: 20px;
            color: #666;
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

# App title
st.markdown('<p class="title">⚖️ BMI & Health Advisor</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Check your Body Mass Index and get personalized advice</p>', unsafe_allow_html=True)

# Input section
st.header("Enter your details")

col1, col2 = st.columns(2)

with col1:
    height_cm = st.number_input("Height (cm)", min_value=50.0, max_value=250.0, value=170.0)

with col2:
    weight_kg = st.number_input("Weight (kg)", min_value=10.0, max_value=300.0, value=65.0)

# Calculate BMI
if st.button("Calculate BMI"):
    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)
    bmi = round(bmi, 2)

    st.subheader("🧮 Your BMI is: " + str(bmi))

    # Health advice
    if bmi < 18.5:
        st.warning("🔎 You are underweight. Try to include more proteins and healthy calories in your diet.")
    elif 18.5 <= bmi < 24.9:
        st.success("✅ You have a healthy weight. Keep maintaining your lifestyle!")
    elif 25 <= bmi < 29.9:
        st.info("📋 You are overweight. Consider regular exercise and balanced meals.")
    else:
        st.error("⚠️ You are obese. It is advised to consult a healthcare provider and make lifestyle changes.")

    st.markdown("---")
    st.caption("🔁 BMI = weight (kg) / (height (m))²")