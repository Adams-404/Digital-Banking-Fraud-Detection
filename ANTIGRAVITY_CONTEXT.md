# Project Handoff — Digital Banking Fraud Detection

## Who I am
Muhammad Adamu Aliyu (Adams / Sudo). Full-Stack & AI/ML Engineer, Gombe Nigeria.
My GitHub: github.com/Adams-404

## What this project is
A 7-week mandatory mentorship group project on Digital Banking Fraud Detection.
Repo: https://github.com/Adams-404/Digital-Banking-Fraud-Detection (my fork of the team lead's repo)

I'm assigned to **Group C (Evaluation & Deployment)** but I'm doing every role myself
to stay sharp — so I need to produce ALL the deliverables below.

## Team structure
- **Sunusi Abdulwahab** — Team Lead & Documentation (also my Group C partner)
- **Group A (Data):** Imran Abdullahi (data collection), Thankgod Israel (cleaning & EDA)
- **Group B (ML):** Giveson Ugwu (feature engineering), Ismaila Abdulsalam (model development)
- **Group C (Evaluation & Deployment):** Muhammad Adamu Aliyu (evaluation), Sunusi (deployment)

## Final deliverables (what must exist by week 7)
1. GitHub repo with all notebooks committed with outputs visible
2. Jupyter/Colab notebooks (one per group role)
3. Trained fraud detection model
4. Streamlit web app deployed on Streamlit Community Cloud
5. Technical report
6. PowerPoint slides

## Repo structure (already cloned at: ~/Projects/Digital-Banking-Fraud-Detection)
```
Digital-Banking-Fraud-Detection/
├── Dataset/
│   ├── bank_transaction_dataset.csv   ← PROBLEM: wrong dataset, see below
│   ├── data_dictionary.xlsx
│   ├── dataset_overview-1.docx
│   ├── problem_statement.docx
│   └── README.md
├── EDA/                    ← empty (just README.md)
├── Feature Engineering/    ← empty (just README.md)
├── Models/                 ← empty (just README.md)
├── Evaluation/             ← empty (just README.md) ← MY primary folder
├── Streamlit-app/          ← empty (just README.md)
├── Documentation/          ← empty
├── Presentation/           ← empty
└── README.md
```

## 🚨 Critical blocker — wrong dataset in repo
The CSV Group A uploaded (`bank_transaction_dataset.csv`, 2512 rows, 16 columns) is from
`valakhorasani/bank-transaction-dataset-for-fraud-detection`. It has NO fraud label column.

Columns present:
```
TransactionID, AccountID, TransactionAmount, TransactionDate, TransactionType,
Location, DeviceID, IP Address, MerchantID, Channel, CustomerAge,
CustomerOccupation, TransactionDuration, LoginAttempts, AccountBalance,
PreviousTransactionDate
```

No IsFraud, no Class, no target variable — can't do supervised ML on this.

The CORRECT dataset is: https://www.kaggle.com/datasets/marusagar/bank-transaction-fraud-detection
That's what the supervisor referenced. It has an `IsFraud` column (0/1).

**Action needed:** Download the correct CSV from Kaggle, rename it appropriately,
and replace the one in Dataset/. I need to flag this to the team lead too.

## Tech stack (per supervisor spec)
| Task | Tool |
|---|---|
| Data Analysis | Pandas |
| Visualization | Matplotlib, Seaborn |
| ML Models | Scikit-learn |
| Imbalanced Data | SMOTE (imbalanced-learn) |
| Gradient Boosting | XGBoost |
| Version Control | Git & GitHub |
| Deployment | Streamlit |
| Docs | Google Docs / MS Word |
| Slides | PowerPoint |

## Models to train (per spec)
- Logistic Regression
- Decision Tree
- Random Forest
- XGBoost

## Evaluation metrics to use (my assigned task — Group C Member 1)
- Accuracy, Precision, Recall, F1 Score, ROC-AUC, Confusion Matrix
- Compare all 4 models, select the best
- Key note: ROC-AUC and Recall matter most — accuracy alone is misleading on imbalanced fraud data

## My environment
- OS: Fedora Workstation (ThinkPad T490s)
- Python: system python3 (pandas just installed with --break-system-packages)
- Packages installed so far: pandas
- Still need: scikit-learn, imbalanced-learn, xgboost, matplotlib, seaborn, streamlit, joblib

## What needs to be built (in order)
Once the correct dataset is in place:

1. **EDA/eda_notebook.ipynb** — cleaning, missing values, duplicates, outlier detection,
   visualizations (class imbalance, distributions, correlation), insights report

2. **Feature Engineering/feature_engineering_notebook.ipynb** — encode categoricals,
   scale numerics, date/time feature extraction, train/test split (stratified),
   SMOTE for class imbalance (only on train set)

3. **Models/model_development_notebook.ipynb** — train all 4 models on SMOTE-resampled
   training data, save trained models with joblib

4. **Evaluation/evaluation_notebook.ipynb** ← MY deliverable — load trained models,
   evaluate on original (non-SMOTE) test set, produce comparison table,
   confusion matrices, ROC curves, pick best model, write evaluation report

5. **Streamlit-app/app.py** — load best model, let user input transaction details,
   predict fraud/legitimate, show confidence score, deploy to Streamlit Community Cloud

## Preferences
- No unnecessary comments or boilerplate — keep code clean and purposeful
- Notebooks should have markdown cells explaining each section (needed for the report)
- Commit each folder's work separately with clear commit messages
- All notebooks should run top-to-bottom without errors before committing
