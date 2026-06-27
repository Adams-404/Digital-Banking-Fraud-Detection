# Digital Banking Fraud Detection

This project provides an end-to-end solution for detecting fraudulent banking transactions using an XGBoost classifier and a Streamlit web application.

## 🚀 Local Setup Instructions

Follow these steps to run the application on your local machine:

### 1. Prerequisites
Ensure you have **Python 3.9+** installed on your system.

### 2. Clone the Repository
```bash
git clone https://github.com/Adams-404/Digital-Banking-Fraud-Detection.git
cd Digital-Banking-Fraud-Detection
```

### 3. Install Dependencies
```bash
pip install -r Streamlit-app/requirements.txt
```

### 4. Run the Streamlit App
```bash
streamlit run Streamlit-app/app.py
```

## 📂 Project Structure
* `Models/`: Contains the trained XGBoost model and training data samples.
* `Streamlit-app/`: Contains the `app.py`, `requirements.txt`, and preprocessing assets (`scaler.pkl`, etc.).
* `Feature Engineering/`: Jupyter notebooks/scripts for data preparation.

## 📊 Model Performance
* **Algorithm**: XGBoost
* **Handling Imbalance**: `scale_pos_weight` optimized for 4% fraud rate.
* **Key Metrics**: Improved fraud recall to ~33% compared to baseline models.
