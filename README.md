# 🛒 BigMart Sales Forecasting Pipeline

This project demonstrates a complete end-to-end **Data Engineering and Machine Learning pipeline** that predicts retail sales using historical data from BigMart. It includes automated ETL, database storage, model training, and deployment via a Streamlit app.

---

## 🚀 Project Highlights

✅ Structured Data Pipeline  
✅ Relational Database (MySQL) Integration  
✅ Data Cleaning & Feature Engineering  
✅ Model Training using Gradient Boosting  
✅ Joblib Model Serialization  
✅ Streamlit App for Prediction  

---

## 🧱 Architecture Overview

```mermaid
graph TD
  A[Raw CSV File] --> B[MySQL Database]
  B --> C[Python Data Processing]
  C --> D[Gradient Boosting Model]
  D --> E[Model Export (joblib)]
  E --> F[Streamlit Web App]
