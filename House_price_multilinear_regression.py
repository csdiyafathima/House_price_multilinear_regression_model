import streamlit as st
import joblib
model = joblib.load("house_price_multilinear_regression.pkl")
st.title("🏠 House Price Prediction")

st.write(
    "Enter the house details to predict the estimated house price."
)
area = st.number_input(
    "📐 Area (sq ft)",
    min_value=500.0,
    max_value=2400.0,
    value=1000.0,
    step=50.0
)

bedrooms = st.number_input(
    "🛏️ Number of Bedrooms",
    min_value=1,
    max_value=5,
    value=2,
    step=1
)

age = st.number_input(
    "🏠 Age of House (years)",
    min_value=1.0,
    max_value=20.0,
    value=5.0,
    step=1.0
)
if st.button("💰 Predict House Price"):

    input_data = [[area, bedrooms, age]]

    prediction = model.predict(input_data)

    predicted_price = prediction[0]

    st.subheader("🏡 Predicted House Price")

    st.success(
        f"💰 Estimated Price: ₹{predicted_price:,.2f}"
    )
