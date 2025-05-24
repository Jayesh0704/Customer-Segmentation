import streamlit as st
import numpy as np
import pickle

# Load trained KMeans model
kmeans = pickle.load(open("kmeans.pkl", 'rb'))

# Clustering function based on RFM input
def clustering(recency, frequency, monetary):
    new_customer = np.array([[recency, frequency, monetary]])
    predicted_cluster = kmeans.predict(new_customer)

    if predicted_cluster[0] == 0:
        return "Lapsed Customer"
    elif predicted_cluster[0] == 1:
        return "Average Customer"
    else:
        return "High-Value Customer (Whale)"

# Streamlit UI
st.title("Customer Segmentation using RFM Clustering")
st.write("Enter the customer's RFM values:")

# RFM inputs
recency = st.number_input("Recency (days since last purchase)", min_value=0, max_value=1000, value=30)
frequency = st.number_input("Frequency (number of purchases)", min_value=0, max_value=100, value=5)
monetary = st.number_input("Monetary Value (total spend)", min_value=0.0, value=500.0)

# Predict cluster
if st.button("Predict Cluster"):
    result = clustering(recency, frequency, monetary)
    st.success(f"The customer belongs to the: **{result}**")

# Footer
st.markdown("---")