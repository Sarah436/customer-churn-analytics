# Customer Churn Analytics

## Project Overview

This project analyzes customer churn using exploratory data analysis, machine learning, explainable AI, and an interactive Power BI dashboard.

The project uses a Telco customer dataset containing 7,043 customer records.

## Key Components

- Exploratory Data Analysis (EDA)
- Data cleaning and preprocessing
- Logistic Regression
- XGBoost
- Model evaluation using Accuracy, Precision, Recall, F1 Score, and ROC-AUC
- XGBoost feature importance
- SHAP-based explainability
- Power BI dashboard
- Python-based live data refresh simulation

## Machine Learning Results

| Model | Accuracy | Precision | Recall | F1 Score | ROC-AUC |
|---|---:|---:|---:|---:|---:|
| Logistic Regression | 0.803 | 0.646 | 0.575 | 0.608 | 0.849 |
| XGBoost | 0.799 | 0.644 | 0.545 | 0.590 | 0.852 |

## Power BI Dashboard

The Power BI dashboard provides:

- Total customers
- Churned customers
- Churn rate
- Average monthly charges
- Average customer tenure
- Churn rate by contract
- Churn rate by internet service
- Churn rate by payment method
- Churn rate by tenure
- Top churn reasons
- ML model performance
- XGBoost feature importance

## Live Data Refresh Simulation

The project includes a Python-based workflow that simulates incoming customer records.

### Workflow

Original Dataset  
↓  
customer_churn_live.csv  
↓  
Python update script  
↓  
New customer records  
↓  
Power BI Refresh  
↓  
Updated Dashboard

### Update Script

The script `src/update_live_data.py` generates new customer records and appends them to the live CSV dataset.

Run from the project root:

```bash
python src/update_live_data.py