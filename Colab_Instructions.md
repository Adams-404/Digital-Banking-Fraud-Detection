# Google Colab Execution & Synchronization Guide

This guide is designed for you and your **Google Colab Gemini AI** to execute the machine learning pipeline notebooks for the **Digital Banking Fraud Detection** project. It outlines how to setup the environment in Colab, run the notebooks in the correct order, and download the resulting trained models back to your local ThinkPad laptop.

---

## 🚀 Step 1: Push Local Code to GitHub (Do this on your ThinkPad first)

Before opening Google Colab, ensure your local changes and dataset are committed and pushed to your GitHub fork. Run these commands in your ThinkPad's terminal:

```bash
# Add all files (notebooks, metadata, and the 68MB CSV dataset)
git add .

# Commit changes
git commit -m "Prepare notebooks and Streamlit app for Colab execution"

# Push to your main branch
git push origin main
```

---

## 📓 Step 2: Open Google Colab & Run Notebooks

### 1. Open the Repository in Colab
1. Open [Google Colab](https://colab.research.google.com).
2. Select the **GitHub** tab.
3. Enter your repository URL: `https://github.com/Adams-404/Digital-Banking-Fraud-Detection`.
4. Click search, and you will see a list of the notebooks in your repository.

---

### 2. Execute `Feature Engineering/feature_engineering.ipynb`
1. Click on **`Feature Engineering/feature_engineering.ipynb`** to open it.
2. At the **very top of the notebook**, create a new code cell, paste the following code, and run it:
   ```python
   # 1. Clone the repository to get the Dataset folder
   !git clone https://github.com/Adams-404/Digital-Banking-Fraud-Detection.git
   
   # 2. Change working directory so relative paths resolve correctly
   %cd Digital-Banking-Fraud-Detection/Feature\ Engineering
   ```
3. Run all cells in the notebook (`Runtime -> Run all` or `Ctrl + F9`).
4. **Save the executed notebook back to GitHub:**
   * Go to **File -> Save a copy in GitHub**.
   * Choose your repository (`Adams-404/Digital-Banking-Fraud-Detection`).
   * Select branch `main`.
   * Click **OK**.
5. **Download the generated preprocessing metadata files:**
   * Click the **Folder icon** on the left-hand sidebar of Colab.
   * Expand the folder: `Digital-Banking-Fraud-Detection` -> `Streamlit-app`.
   * Right-click and download the following files:
     * `categorical_options.pkl`
     * `feature_columns.pkl`
     * `numeric_columns.pkl`
     * `scaler.pkl`
   * Place these files in your local `/home/adam/Projects/Digital-Banking-Fraud-Detection/Streamlit-app/` directory (replacing old ones).

---

### 3. Execute `Models/model_training.ipynb`
1. Close the previous Colab tab. Go back to Colab home, select the **GitHub** tab again, and open **`Models/model_training.ipynb`**.
2. At the **very top of the notebook**, create a new code cell, paste the following code, and run it:
   ```python
   # 1. Clone the repository to get the Dataset and saved data folders
   !git clone https://github.com/Adams-404/Digital-Banking-Fraud-Detection.git
   
   # 2. Change working directory so relative paths resolve correctly
   %cd Digital-Banking-Fraud-Detection/Models
   ```
3. Run all cells in the notebook (`Runtime -> Run all` or `Ctrl + F9`).
4. **Save the executed notebook back to GitHub:**
   * Go to **File -> Save a copy in GitHub** (select `main` branch, click OK).
5. **Verify trained models exist in Colab:**
   * Look in the file explorer under `Digital-Banking-Fraud-Detection/Models/`. You should see the trained model pickle files:
     * `logistic_regression.pkl`
     * `decision_tree.pkl`
     * `random_forest.pkl`
     * `xgboost.pkl`
   * *Note: You do not need to download these individual models yet; the next notebook (Evaluation) will process them.*

---

### 4. Execute `Evaluation/model_evaluation.ipynb`
1. Close the tab. Go back to Colab home, select the **GitHub** tab, and open **`Evaluation/model_evaluation.ipynb`**.
2. At the **very top of the notebook**, create a new code cell, paste the following code, and run it:
   ```python
   # 1. Clone the repository
   !git clone https://github.com/Adams-404/Digital-Banking-Fraud-Detection.git
   
   # 2. Copy the trained model files from your GitHub repository
   # Note: Since the previous step committed them to GitHub, we clone the updated repository
   %cd Digital-Banking-Fraud-Detection/Evaluation
   ```
   *If the models are not yet pushed to GitHub, you can manually upload them into the `/content/Digital-Banking-Fraud-Detection/Models` directory in Colab using the file explorer sidebar upload button.*
3. Run all cells in the notebook (`Runtime -> Run all` or `Ctrl + F9`).
4. **Save the executed notebook back to GitHub:**
   * Go to **File -> Save a copy in GitHub** (select `main` branch, click OK).
5. **Download the Best Model for Streamlit Deployment:**
   * In the Colab file explorer, go to `Digital-Banking-Fraud-Detection/Streamlit-app/` and download **`fraud_model.pkl`**.
   * Place this file in your local `/home/adam/Projects/Digital-Banking-Fraud-Detection/Streamlit-app/` directory.
   * Go to `Digital-Banking-Fraud-Detection/Models/` and download the other model files if you wish to store them locally:
     * `logistic_regression.pkl`
     * `decision_tree.pkl`
     * `random_forest.pkl`
     * `xgboost.pkl`

---

## 💻 Step 3: Pull Changes and Run Streamlit Locally (On your ThinkPad)

Once all notebooks have been executed and saved back to GitHub:

1. **Pull the executed notebooks down to your local machine:**
   Open a terminal in your workspace `/home/adam/Projects/Digital-Banking-Fraud-Detection` and run:
   ```bash
   git pull origin main
   ```
2. **Verify downloaded files in `Streamlit-app/`:**
   Ensure the following files are present on your ThinkPad:
   * `app.py`
   * `requirements.txt`
   * `categorical_options.pkl`
   * `feature_columns.pkl`
   * `numeric_columns.pkl`
   * `scaler.pkl`
   * `fraud_model.pkl`
3. **Run the Streamlit application:**
   Activate your virtual environment and run the app:
   ```bash
   source .venv/bin/activate
   streamlit run Streamlit-app/app.py
   ```
