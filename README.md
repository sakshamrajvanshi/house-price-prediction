# 🏠 House Price Prediction (ML Web App)

This is a Machine Learning web application built using **Flask** that predicts house prices based on user input. It uses a **Linear Regression** model trained on the Boston Housing dataset.

> 📌 This project was developed as part of a **college group project** for academic purposes.

---

## 🚀 Features

- Predicts house prices using 13 numerical input features  
- Trained using Scikit-learn's Linear Regression  
- Simple UI built with HTML and CSS  
- Model saved using `pickle` and loaded into a Flask app  

---

## 📂 Project Structure

house-price-prediction/
│
├── app/
│ ├── app.py # Flask app
│ └── templates/
│ └── index.html # Frontend UI
│
├── notebook/
│ ├── model_dev.ipynb # Jupyter notebook for model training
│ └── model/
│ └── price_model.pkl # Trained ML model
│
├── data/
│ └── housing.csv # Dataset used
│
└── README.md


---

## 🧠 Technologies Used

- Python  
- Pandas, NumPy  
- Scikit-learn  
- Flask  
- HTML/CSS  

---

## 🛠 How to Run Locally

1. **Clone the repository**
   git clone https://github.com/sakshamrajvanshi/house-price-prediction.git
   cd house-price-prediction

2. **Install dependencies**
   pip install -r requirements.txt

3. **Run the app**
   cd app
   python app.py

4. **Visit in your browser**  
   http://127.0.0.1:5000

Note

This is a basic educational project.

The dataset used (housing.csv) is based on the Boston Housing dataset.

Model may not generalize well to real-world use cases.
