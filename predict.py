import streamlit as st
import pickle
import numpy as np
import pandas as pd


def load_model():
    model = pickle.load(open("model.pkl", "rb"))

    return model

model = load_model()

def show_predict_page():
    st.title("Credit Card Fraud Detection")
    st.write("""### We need some information to predict if the transaction is fraud""")
    
    # Create input fields for the numerical columns
    distance_from_home = st.number_input('Distance from Home')
    distance_from_last_transaction = st.number_input('Distance from Last Transaction')
    ratio_to_median_purchase_price = st.number_input('Ratio to Median Purchase Price')
    repeat_retailer = st.radio('Repeat Retailer', [0, 1])
    used_chip = st.radio('Used Chip', [0, 1])
    used_pin_number = st.radio('Used Pin Number', [0, 1])
    online_order = st.radio('Online Order', [0, 1])

    # Create a dictionary from the input values
    input_dict = {
        'distance_from_home': distance_from_home,
        'distance_from_last_transaction': distance_from_last_transaction,
        'ratio_to_median_purchase_price': ratio_to_median_purchase_price,
        'repeat_retailer': repeat_retailer,
        'used_chip': used_chip,
        'used_pin_number': used_pin_number,
        'online_order': online_order
    }

    # Convert the input dictionary to a Pandas DataFrame
    input_df = pd.DataFrame([input_dict])

    # Use the trained model to make predictions on the input data
    prediction = model.predict(input_df)

    # Show the predicted result
    if prediction[0]:
        st.write('This transaction is Fraud')
    else: st.write('This transaction is Safe')
    

   