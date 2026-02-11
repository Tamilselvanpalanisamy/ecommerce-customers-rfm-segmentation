# 📊 E-commerce Customer Segmentation using RFM Analysis

## 📌 Project Overview
This project focuses on **Customer Segmentation using RFM (Recency, Frequency, Monetary) Analysis** on an e-commerce transaction dataset.  
The goal is to analyze customer purchasing behavior and segment customers into meaningful groups for business decision-making.

---

## 🎯 Problem Statement
E-commerce businesses need to:
- Identify high-value customers
- Retain loyal customers
- Detect at-risk and inactive customers

RFM analysis helps address these challenges by categorizing customers based on transaction history.

---

## 🧠 What is RFM Analysis?
- **Recency (R):** Days since the customer's last purchase  
- **Frequency (F):** Number of purchases made by the customer  
- **Monetary (M):** Total amount spent by the customer  

Each metric helps measure customer value.

---

## 🛠️ Tools & Technologies Used
- Python  
- Pandas  
- NumPy  
- VS Code  

---

## 📂 Dataset Description
The dataset contains e-commerce transaction data including:
- Invoice number  
- Customer ID  
- Quantity  
- Invoice date  
- Unit price  

---

## 🧹 Data Cleaning
The following steps were performed:
- Removed rows with missing **CustomerID**
- Removed transactions with **negative quantity**
- Created `TotalAmount = Quantity × UnitPrice`
- Converted date columns to datetime format

---

## 📐 RFM Calculation
- **Recency:** Days since last purchase from a reference date  
- **Frequency:** Count of unique invoices per customer  
- **Monetary:** Total spending per customer  

---

## 📊 RFM Scoring
- Quantile-based scoring (1–5) applied to R, F, and M
- Higher scores indicate higher customer value
- Combined to form an overall **RFM Score**

---

## 🧩 Customer Segmentation
Customers were segmented into:
- Champions  
- Loyal Customers  
- Potential Loyalists  
- At Risk  
- Lost Customers  

Each segment represents a distinct purchasing behavior.

---

## 📈 Final Output
The final dataset includes:
- Recency
- Frequency
- Monetary
- RFM Scores
- Customer Segment

---

## 💼 Business Value
- Identifies high-value customers
- Enables targeted marketing
- Improves customer retention
- Supports data-driven decisions

---

## 🚀 Future Enhancements
- Power BI dashboard
- Visual analysis of segments
- Advanced clustering techniques

---

## 👤 Author
**Tamilselvan**  
Aspiring Data Analyst  
Email:tamilpalanisamy1103@gmail.com
LinkedIn:www.linkedin.com/in/tamilselvanp1103


