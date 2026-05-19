# 🌦️ Weather Prediction System

A Machine Learning based Weather Prediction System built using Flask, Python, and Scikit-learn that predicts weather conditions such as minimum temperature, maximum temperature, average temperature, and precipitation based on a given date.

---

## 🚀 Features

- 🌡️ Predicts:
  - Minimum Temperature (tmin)
  - Maximum Temperature (tmax)
  - Average Temperature (tavg)
  - Precipitation (prcp)

- 📅 Date-based prediction system
- 🤖 Machine Learning model using Linear Regression
- 🌐 Flask web application
- 🎨 Responsive frontend UI
- 📊 Weather dataset analysis and visualization

---

## 🛠️ Tech Stack

### Frontend
- HTML5
- CSS3

### Backend
- Python
- Flask

### Machine Learning
- Scikit-learn
- Pandas
- NumPy
- Matplotlib

---

## 📂 Project Structure

```bash
Weather-Prediction-System/
│
├── static/
│   └── styles.css
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── weather prediction.ipynb
├── weather_model.pkl
├── mumbai.csv
├── app.py
├── requirements.txt
├── README.md
└── screenshots/
```

---

## 📊 Dataset

The project uses a Mumbai weather dataset containing:

- Date
- Average Temperature
- Minimum Temperature
- Maximum Temperature
- Precipitation

Dataset File:
```bash
mumbai.csv
```

---

## 🧠 Machine Learning Model

### Algorithm Used
- Linear Regression

### Input Features
- Month
- Day
- Year

### Target Variables
- tmin
- tmax
- tavg
- prcp

---

## ⚙️ Model Training Workflow

1. Load dataset
2. Clean missing values
3. Extract date features
4. Train Linear Regression model
5. Save trained model using Pickle
6. Deploy with Flask

---

## 📈 Model Evaluation

| Metric | Value |
|---|---|
| Mean Squared Error | 263.58 |
| R² Score | 0.08 |

---

## 🔄 Application Workflow

1. User enters a date
2. Flask receives input
3. ML model predicts weather
4. Results displayed on webpage

---

## 🖥️ User Interface

### Home Page
- Enter date in DD-MM-YYYY format
- Click Predict button

### Prediction Page
Displays:
- Minimum Temperature
- Maximum Temperature
- Average Temperature
- Precipitation

---

## 📸 Screenshots

### 🏠 Home Page

<p align="center">
  <img src="screenshots/home.png" width="850"/>
</p>

---

### 📊 Prediction Results

<p align="center">
  <img src="screenshots/result.png" width="850"/>
</p>

---

### 📈 Dataset Visualization

<p align="center">
  <img src="screenshots/graph.png" width="850"/>
</p>

---

## ▶️ How to Run

### 1️⃣ Clone Repository

```bash
git clone https://github.com/KaranBisht111/Weather-Prediction-System.git
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Run Flask Application

```bash
python app.py
```

---

### 4️⃣ Open Browser

```bash
http://127.0.0.1:5000/
```

---

## 📦 Requirements

- Python 3.x
- Flask
- NumPy
- Pandas
- Scikit-learn
- Matplotlib

---

## 🔮 Future Enhancements

- Deep Learning weather forecasting
- Real-time API integration
- Multi-city prediction
- Weather visualization dashboard
- Accuracy improvement using advanced models
- LSTM/Random Forest implementation

---

## 📚 Learning Outcomes

This project demonstrates:

- Machine Learning workflow
- Data preprocessing
- Regression modeling
- Flask deployment
- Data visualization
- Model serialization using Pickle

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

Karan Bisht

---

## ⭐ Support

If you found this project useful, give it a star on GitHub ⭐