# Customer-Segmentation
# 📊 RFM Customer Segmentation App

This is a Streamlit web app that uses **RFM (Recency, Frequency, Monetary)** analysis and a trained **KMeans clustering model** to segment customers into behavioral groups. It helps businesses understand their customer base and target marketing strategies accordingly.

🔗 **Live App**: [rfmdashboard.streamlit.app](https://rfmdashboard.streamlit.app/)

---

## 🚀 Features

- Input **RFM values** (Recency, Frequency, Monetary).
- Get predicted **customer segment** using a trained KMeans clustering model.
- Categories:
  - 🧊 **Lapsed Customer**
  - ⚖️ **Average Customer**
  - 🐋 **High-Value Customer (Whale)**

---

## 📁 Project Structure

.
├── app.py # Streamlit app
├── kmeans.pkl # Trained KMeans clustering model
├── RFM.ipynb # Notebook for RFM analysis and model training
├── requirements.txt # Python dependencies
└── README.md # Project documentation

## 🧠 How It Works

1. The notebook `RFM.ipynb` performs:
   - RFM score calculation from customer purchase data.
   - Normalization & KMeans clustering.
   - Saving the trained model to `kmeans.pkl`.

2. The `app.py` Streamlit app:
   - Accepts user input for R, F, M values.
   - Loads the `kmeans.pkl` model using `joblib`.
   - Predicts and displays the customer cluster.

---

## 🛠 Installation (for local use)

```bash
git clone https://github.com/<your-username>/rfm-customer-segmentation.git
cd rfm-customer-segmentation
pip install -r requirements.txt
streamlit run app.py


