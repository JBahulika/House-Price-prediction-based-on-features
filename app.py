import pandas as pd
import streamlit as st
import joblib

# Load trained model
model = joblib.load('xgb_model.jb')

# Streamlit app title
st.title("🏠 House Price Prediction")
st.write("Enter details below to predict the estimated house price:")


#  Define Display Names 

display_features = [
    'OverallQuality(1-10)',
    'Ground Living Area',
    'GarageArea',
    'First Floor Square Feet',
    'The number of fully equipped bathrooms',
    'Year Built',
    'Year of Remodel or Addition',
    'Masonry Veneer Area',
    'Number of Fireplaces',
    'Basement Finished Area',
    'Lot Frontage',
    'WoodDeck Square Feet',
    'Open Porch Square Feet',
    'Lot Area',
    'CentralAir(Yes/No)'
]

#  Mapping Display → Actual Model Feature Names

feature_mapping = {
    'OverallQuality(1-10)': 'OverallQual',
    'Ground Living Area': 'GrLivArea',
    'GarageArea': 'GarageArea',
    'First Floor Square Feet': '1stFlrSF',
    'The number of fully equipped bathrooms': 'FullBath',
    'Year Built': 'YearBuilt',
    'Year of Remodel or Addition': 'YearRemodAdd',
    'Masonry Veneer Area': 'MasVnrArea',
    'Number of Fireplaces': 'Fireplaces',
    'Basement Finished Area': 'BsmtFinSF1',
    'Lot Frontage': 'LotFrontage',
    'WoodDeck Square Feet': 'WoodDeckSF',
    'Open Porch Square Feet': 'OpenPorchSF',
    'Lot Area': 'LotArea',
    'CentralAir(Yes/No)': 'CentralAir'
}

# Dictionary to store user input
input_data = {}


# Collect User Inputs

for feature in display_features:
    if feature == 'CentralAir(Yes/No)':
        input_data[feature] = st.selectbox(feature, options=['Yes', 'No'], index=0)
    else:
        input_data[feature] = st.number_input(feature, value=0.0, step=0.1)


#  Predict Button

if st.button("Predict Price"):
    # Convert display names to actual feature names
    processed_input = {}
    for display_name, value in input_data.items():
        actual_name = feature_mapping[display_name]
        processed_input[actual_name] = value

    # Convert Yes/No to 1/0
    processed_input['CentralAir'] = 1 if processed_input['CentralAir'] == 'Yes' else 0

    # Prepare dataframe with correct feature order
    model_features = [
        'OverallQual', 'GrLivArea', 'GarageArea', '1stFlrSF',
        'FullBath', 'YearBuilt', 'YearRemodAdd', 'MasVnrArea',
        'Fireplaces', 'BsmtFinSF1', 'LotFrontage', 'WoodDeckSF',
        'OpenPorchSF', 'LotArea', 'CentralAir'
    ]

    input_df = pd.DataFrame([processed_input], columns=model_features)

    # Make prediction
    predictions = model.predict(input_df)

    # Show result
    st.success(f"🏡 Predicted House Price: **${predictions[0]:,.2f}**")
