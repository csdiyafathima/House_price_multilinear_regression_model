import streamlit as st
import joblib
model = joblib.load("House_price_multilinear_regression.pkl")
st.title(" House Price Prediction")

st.write(
    "Enter the house details to predict the estimated house price."
)
area = st.number_input(
    " Area (sq ft)",
    min_value=500.0,
    max_value=2400.0,
    value=1000.0,
    step=50.0
)

bedrooms = st.number_input(
    "Number of Bedrooms",
    min_value=1,
    max_value=5,
    value=2,
    step=1
)

age = st.number_input(
    " Age of House (years)",
    min_value=1.0,
    max_value=20.0,
    value=5.0,
    step=1.0
)
if st.button("Predict"):
    if area < 200:
        st.error("Area cannot be less than 200.")
    
    elif area > 600:
        st.error("Area cannot be more than 600.")
    elif bedrooms < 1:
        st.error("Number of bedrooms must be at least 1.")

    elif bedrooms > 7:
        st.error("Number of bedrooms cannot be more than 7.")
    elif age < 5:
        st.error("House age cannot be less than 5 years.")

    elif age > 25:
        st.error("House age cannot be more than 25 years.")

    else:
        prediction = model.predict([[area, bedrooms, age]])

        st.success(
            f"Predicted House Price: ${prediction[0]:,.2f}"
        )
