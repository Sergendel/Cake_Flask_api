# Cake Price Prediction API 🍰

This repository contains a Flask-based API designed to predict cake prices using historical sales data and machine learning models.

## Overview

The Cake Price Prediction API provides endpoints to estimate cake prices based on various features. 
By leveraging trained machine learning models, it offers dynamic pricing predictions to assist in decision-making.

## Project structire
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
    
2. **API endpoint and request example:**
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