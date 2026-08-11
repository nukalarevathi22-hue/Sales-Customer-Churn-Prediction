# Sales-Customer-Churn-Prediction

## 📌 Project Overview

Customer churn is a major challenge for businesses because losing customers can directly affect revenue and long-term growth. This project uses **Machine Learning** to analyze customer information and predict whether a customer is likely to churn.

The project includes data preprocessing, exploratory analysis, model building, model evaluation, and feature-importance analysis to understand the factors that contribute to customer churn.

---

## 🎯 Objectives

* Analyze customer data and identify patterns related to churn.
* Perform data preprocessing and prepare the dataset for Machine Learning.
* Explore customer and service-related features.
* Build a Machine Learning classification model.
* Evaluate the model's performance.
* Identify important features influencing customer churn.
* Predict churn for a new customer.

---

## 🛠️ Technologies Used

* **Python**
* **Pandas**
* **NumPy**
* **Matplotlib**
* **Seaborn**
* **Scikit-learn**
* **Jupyter Notebook**

---

## 📂 Project Structure

```text
Sales-Customer-Churn-Prediction/
│
├── Sales_Customer_Churn.ipynb
├── sales customer churn project.html
├── dataset/
│   └── customer_churn.csv
├── images/
│   └── project_visualizations/
├── project_documentation.pdf
├── Sales_Customer_Churn_Presentation.pptx
├── requirements.txt
└── README.md
```

---

## 🔄 Project Workflow

```text
Data Collection
      ↓
Data Cleaning & Preprocessing
      ↓
Exploratory Data Analysis
      ↓
Feature Preparation
      ↓
Machine Learning Model
      ↓
Model Evaluation
      ↓
Feature Importance Analysis
      ↓
Customer Churn Prediction
```

---

## 🧹 Data Preprocessing

The customer data is prepared before applying the Machine Learning model. The project uses customer-related features such as:

* Contract Type
* Internet Service
* Payment Method
* Tenure
* Monthly Charges
* Total Charges

The processed features are then used as input for the Machine Learning model.

---

## 🤖 Machine Learning

A classification-based Machine Learning approach is used to predict customer churn.

The trained model is evaluated using classification metrics. The project obtained an overall accuracy of approximately **74%** on the evaluated dataset.

> **Note:** Accuracy alone should not be considered sufficient for evaluating a churn model, especially when the classes are imbalanced. The classification report also shows differences between the evaluation metrics for the classes.

---

## 🔍 Feature Importance

Feature importance is analyzed to understand **why customers may churn**. The project uses the model coefficients to examine the contribution of the input features to the prediction.

This helps businesses identify customer characteristics that may require attention for improving customer retention.

---

## 🔮 Customer Churn Prediction

The trained model can be used to make predictions for a new customer.

The project demonstrates a new customer input containing:

* Contract Type
* Internet Service
* Payment Method
* Tenure
* Monthly Charges
* Total Charges

The processed customer information is passed to the trained model to generate a churn prediction.

---

## 📈 Model Evaluation

The model achieved:

**Accuracy: ~74%**

The classification report was also used to evaluate precision, recall, and F1-score for the prediction classes.

---

## 💡 Key Insights

* Customer-related and service-related features can be used to identify churn patterns.
* Machine Learning can assist businesses in identifying customers who may be at risk of leaving.
* Feature importance can help understand the factors contributing to churn.
* Churn prediction can support customer-retention strategies.

---

## 🚀 Future Improvements

* Test multiple Machine Learning algorithms.
* Handle class imbalance using suitable techniques.
* Perform hyperparameter tuning.
* Improve model evaluation using additional metrics such as ROC-AUC.
* Build an interactive dashboard for churn analysis.
* Deploy the model as a web application or API.

---

## 📌 Conclusion

This project demonstrates how Machine Learning can be applied to **customer churn prediction**. By preprocessing customer data, analyzing patterns, building a classification model, and studying feature importance, businesses can gain useful insights into customer behavior and identify customers who may be at risk of churn.

---

## 👩‍💻 Author

**Revathi Nukala**


