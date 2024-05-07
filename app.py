import streamlit as st
import pandas as pd
import pickle as pkl

# Load pre-trained model
with open('csk.pkl', 'rb') as f:
    model = pickle.load(f)

# Streamlit app
st.title('ATS Car Price Predictor')

# Input fields for user to enter car features
company_name = st.selectbox('Company Name', ['Adam', 'Audi', 'BMW', 'Chery', 'Chevrolet', 'DFSK', 'Daewoo', 'Daihatsu', 'FAW', 'Fiat', 'Honda', 'Hummer', 'Hyundai', 'Jaguar', 'Jeep', 'KIA', 'Land', 'Lexus', 'MINI', 'Mazda', 'Mercedes', 'Mitsubishi', 'Nissan', 'Porsche', 'Range', 'SsangYong', 'Subaru', 'Suzuki', 'Toyota', 'United', 'Volvo'])
model_name = st.text_input('Model Name')
model_year = st.number_input('Model Year', min_value=1900, max_value=2024, value=2022, step=1)
location = st.selectbox('Location', ['Location A', 'Location B', 'Location C'])
mileage = st.number_input('Mileage (in km)', min_value=0, value=0, step=1000)
engine_type = st.selectbox('Engine Type', ['Petrol', 'Diesel', 'Electric'])
engine_capacity = st.number_input('Engine Capacity (in cc)', min_value=500, value=1500, step=100)
color = st.selectbox('Color', ['Assembly', 'Beige', 'Black', 'Blue', 'Bronze', 'Brown', 'Burgundy', 'Gold', 'Green', 'Grey', 'Indigo', 'Magenta', 'Maroon', 'Navy', 'Orange', 'Pink', 'Purple', 'Red', 'Silver', 'Turquoise', 'Unlisted', 'White', 'Wine', 'Yellow'])
assembly = st.selectbox('Assembly', ['Local', 'Imported'])
body_type = st.selectbox('Body Type', ['Sedan', 'Hatchback', 'SUV', 'Convertible', 'Other'])
transmission_type = st.selectbox('Transmission Type', ['Automatic', 'Manual'])

# Predict button
if st.button('Predict'):
    # Prepare input data for prediction
    features = {
        'Company Name': company_name,
        'Model Name': model_name,
        'Model Year': model_year,
        'Location': location,
        'Mileage': mileage,
        'Engine Type': engine_type,
        'Engine Capacity': engine_capacity,
        'Color': color,
        'Assembly': assembly,
        'Body Type': body_type,
        'Transmission Type': transmission_type
    }
    
    # Convert features to DataFrame
    input_df = pd.DataFrame([features])
    
    # Make prediction
    predicted_price = model.predict(input_df)[0]
    
    # Display prediction
    st.subheader(f'Predicted Price: {predicted_price:.2f}')
