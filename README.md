# 🛒 BigMart Sales Forecasting Pipeline

This project demonstrates a complete end-to-end **Data Engineering and Machine Learning pipeline** that predicts retail sales using historical data from BigMart. It includes automated ETL, database storage, model training, and deployment via a Streamlit app.



## 🚀 Project Highlights

✅ Structured Data Pipeline  
✅ Relational Database (MySQL) Integration  
✅ Data Cleaning & Feature Engineering  
✅ Model Training using Gradient Boosting  
✅ Joblib Model Serialization  
✅ Streamlit App for Prediction  



## 🧱 Architecture Overview

```mermaid
flowchart TD
    subgraph Ingestion [📥 Data Ingestion]
        A1[📄 df_item.csv] --> A4[(MySQL: item_info)]
        A2[📄 df_outlet.csv] --> A5[(MySQL: outlet_info)]
        A3[📄 df_sales.csv] --> A6[(MySQL: sales_info)]
    end

    subgraph Processing [⚙️ Data Processing]
        A4 --> B1[🔗 Merge Tables]
        A5 --> B1
        A6 --> B1
        B1 --> B2[🧹 Cleaning & Feature Engineering]
        B2 --> B3[🔀 Train/Test Split]
    end

    subgraph Modeling [🤖 Model Training]
        B3 --> C1[📈 GradientBoostingRegressor]
        C1 --> C2[💾 Save bigmart_model.joblib]
    end

    subgraph Deployment [🚀 Streamlit App]
        C2 --> D1[🌐 Streamlit Web Interface]
        D1 --> D2[📊 Predict Sales]
    end
