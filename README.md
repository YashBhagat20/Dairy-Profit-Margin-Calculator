# Dairy Profit Margin Calculator

## Candidate Details

| Field | Details |
|-------|---------|
| **Full Name** | Yash Bhagat |
| **Email ID** | yashbhagat2524@gmail.com |
| **College Name** | Zeal College of Engineering & Research |
| **Selected Skill Track** | AI & Machine Learning |

---

## Project Overview

A production-ready REST API that predicts daily and monthly profit margins for dairy farmers based on milk production and operational costs.

---

## Live API

🔗 https://dairy-profit-margin-calculator.onrender.com  
📄 Swagger Docs: https://dairy-profit-margin-calculator.onrender.com/docs

---

## Tech Stack

- **Language**: Python 3.12
- **Framework**: FastAPI
- **Server**: Uvicorn
- **Validation**: Pydantic
- **Deployment**: Render

---

## API Endpoint

### `POST /predict-profit`

**Request Body:**
```json
{
  "cow_milk": 50.0,
  "buffalo_milk": 30.0,
  "healthcare_cost": 200.0,
  "transport_cost": 150.0,
  "helper_cost": 300.0,
  "machinery_cost": 100.0
}
```

**Response:**
```json
{
  "milk_distribution": {
    "customers_litres": 26.67,
    "suppliers_litres": 26.67,
    "vendors_litres": 26.67
  },
  "revenue": {
    "customer_revenue": 1920.0,
    "supplier_revenue": 3840.0,
    "vendor_revenue": 2720.0,
    "total_revenue": 8480.0
  },
  "daily_profit": 7730.0,
  "monthly_prediction": 231900.0
}
```

---

## Business Logic

- Milk is distributed equally across **3 channels**: Customers, Suppliers, Vendors
- Pricing per litre: Customers ₹72 | Suppliers ₹144 | Vendors ₹102
- Daily costs: Healthcare + Transport + Helper + Machinery
- **Monthly Prediction** = Daily Profit × 30

---

## How to Run Locally
```bash
git clone https://github.com/YashBhagat20/Dairy-Profit-Margin-Calculator
cd Dairy-Profit-Margin-Calculator
pip install -r requirements.txt
uvicorn main:app --reload
```
