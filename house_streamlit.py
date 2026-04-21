import streamlit as st
import pickle

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.title("🏠 House Price Prediction")

# Inputs
area = st.number_input("Area")
bedrooms = st.number_input("Bedrooms")
bathrooms = st.number_input("Bathrooms")
stories = st.number_input("Stories")

mainroad = st.selectbox("Main Road", ["yes", "no"])
guestroom = st.selectbox("Guest Room", ["yes", "no"])
basement = st.selectbox("Basement", ["yes", "no"])
hotwaterheating = st.selectbox("Hot Water Heating", ["yes", "no"])
airconditioning = st.selectbox("Air Conditioning", ["yes", "no"])
prefarea = st.selectbox("Preferred Area", ["yes", "no"])

parking = st.number_input("Parking")

furnishing = st.selectbox(
    "Furnishing",
    ["furnished", "semi-furnished", "unfurnished"]
)

# Convert yes/no → 1/0
binary_map = {"yes": 1, "no": 0}

mainroad = binary_map[mainroad]
guestroom = binary_map[guestroom]
basement = binary_map[basement]
hotwaterheating = binary_map[hotwaterheating]
airconditioning = binary_map[airconditioning]
prefarea = binary_map[prefarea]

# One-hot encoding for furnishing
furnished = 1 if furnishing == "furnished" else 0
semi = 1 if furnishing == "semi-furnished" else 0
unfurnished = 1 if furnishing == "unfurnished" else 0

# Predict
if st.button("Predict"):
    features = [[
        area, bedrooms, bathrooms, stories,
        mainroad, guestroom, basement,
        hotwaterheating, airconditioning,
        parking, prefarea,
        furnished, semi, unfurnished
    ]]

    result = model.predict(features)
    st.success(f"Predicted Price: ₹{int(result[0])}")