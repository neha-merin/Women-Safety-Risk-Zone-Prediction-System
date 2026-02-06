# 🚺 Women Safety Risk Zone Prediction System – Demo Version

This repository contains a demo prototype of the Women Safety Risk Zone Prediction System.

It demonstrates how crime-related location data can be visualized using heatmaps to identify high-risk areas for women’s safety. This version represents a simplified working model of the full-scale system.

---

## 🎯 Purpose of This Demo

This demo is built to:

- Validate heatmap-based risk visualization
- Demonstrate Flask web integration
- Show data-driven safety insights

It acts as a proof-of-concept for the complete solution.

---

## 📌 Features in Demo

- 📍 Location-based risk visualization  
- 🔥 Interactive heatmap using Folium  
- 📊 Preloaded dataset (no upload required)  
- 🌐 Flask web interface  

---

## 🛠 Tech Stack

Backend:
- Python  
- Flask  
- Pandas  

Visualization:
- Folium  

Frontend:
- HTML (Flask templates)

---

## 📂 Project Structure

women_safety_flask/
│
├── app.py  
├── data.csv  
│
├── templates/  
│   └── dashboard.html  
│
└── static/  
    └── heatmap.html  

---

## ▶️ How to Run the Demo

Install dependencies:

pip install flask pandas folium

Run the app:

python app.py

Open in browser:

http://127.0.0.1:5000

---

## 📊 Dataset Format

The demo dataset contains:

Latitude, Longitude, Risk_Score

Risk_Score ranges from 0 (low risk) to 1 (high risk).

---

## 🔮 Planned Full Version Features

- Time-based risk analysis  
- Crime type impact modeling  
- Explainable risk factors  
- City-wise visualization  
- SOS & emergency features  
- Mobile-friendly UI  

---

## 📘 Project Note

This demo serves as a prototype to showcase the feasibility of a women safety risk prediction system using data visualization and web technologies.

The complete version will include real-world datasets and advanced analytics.

---

## 📜 License

For educational and demonstration purposes only.
