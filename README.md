# Cake Price Prediction API 🍰

This repository contains a Flask-based API designed to predict cake prices using historical sales data and machine learning models.

## Overview

The Cake Price Prediction API provides endpoints to estimate cake prices based on various features. 
By leveraging trained machine learning models, it offers dynamic pricing predictions to assist in decision-making.

# API Endpoints
## 1. Cake Price Prediction: /predict

Accepts three parameters: radius (float), layers (integer), and topping (string), and returns a predicted cake price.

### Request Example:

   ```bash
  {
  "Radius [cm]": 5,
  "Layers": 2,
  "Topping": "Picture" // options: ['Picture', 'Writing', 'Extreme', 'Simple', 'Decorative']
  }   
   ```
### Response Example:

   ```bash
   {
   "predict_result": 120
   }
```

## 2. Topping Recommendations: /toppings

Description:
Accepts two parameters: radius (float) and layers (integer). 
Returns a list of five recommended toppings along with their predicted prices.

### Request Example:
   ```bash
   { 
   "Radius [cm]": 5,
   "Layers": 2
   }  
   ```

### Response Example:
   ```bash
   {
   "recommendations": [
   {"topping": "Simple", "predicted_price": 25},
   {"topping": "Writing", "predicted_price": 30},
   {"topping": "Decorative", "predicted_price": 35},
   {"topping": "Picture", "predicted_price": 40},
   {"topping": "Extreme", "predicted_price": 50}
   ]
   }  
   ```



## 3. Model Information: /model-info
Does not accept any parameters.
Returns information about the machine learning model used for cake price prediction.

### Response Example:
   ```bash
   {
  "python_version": "3.11.5",
  "model_version": "1.0",
  "description": "Cake Price Prediction Model using radius, layers, and topping."
   }  
   ```

# Swagger Documentation

Swagger UI for interactive API documentation is available at:

http://localhost:8000/swagger/


## Project structire
   ```bash
   Cake_Flask_api/
   ├── data/
   │   └── cakes.csv                # Historical sales data
   ├── extract/
   │   └── extract_base.py          # base class for data extraction
   │   └── extract_file.py          # file extraction
   │   └── OneHotEncoder.pkl        # pretrained one ot encoder
   ├── models/
   │   └── model.pkl                # Trained machine learning model
   ├── notebook/
   │   └── analysis.ipynb           # Jupyter Notebook for data analysis
   ├── schemas/
   │   └── cake_schema.py           # Data validation schemas
   ├── transform/
   │   └── transform_model.py       # model transformation 
   │   └── transform_processing.py  # data transformation 
   ├── api.py                       # API route definitions
   ├── config.py                    # Configuration settings
   ├── main.py                      # Main skript
   ├── requirements.txt             # Python dependencies
   └── README.md                    # Project documentation
   ```

## Tech Stack

- **Flask** – A lightweight Python web framework.
- **scikit-learn** – A machine learning library for Python.
- **pandas** – A data manipulation and analysis library.
- **NumPy** – A library for numerical computations in Python.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Sergendel/Cake_Flask_api.git
   cd Cake_Flask_api
   ```
    
2. **Example API Request::**
   ```bash
   POST http://127.0.0.1:8000/predict
   body: 
   {
     "Layers": 1,
     "Topping":"Picture",
     "Price": 311
     }
    content-typeL application/json 
   ```