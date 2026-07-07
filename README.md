# OptiCrop 🌾 — Smart Crop Recommendation System

OptiCrop is a machine learning-powered web application designed to help farmers optimize agricultural productivity. By analyzing environmental and soil parameters, the system accurately recommends the most suitable crop to cultivate, maximizing yield and resource efficiency.

---

## 🚀 Features

* **High-Accuracy ML Model:** Powered by a tuned Random Forest Classifier achieving **99.32% accuracy**.
* **Interactive Web Interface:** A clean, user-friendly Flask front-end for real-time predictions.
* **Instant Insights:** Input soil and weather data to receive an immediate crop recommendation.

---

## 📁 Repository Structure

```text
OptiCrop/
│
├── dataset/            # Contains the Crop_recommendation.csv dataset
├── model/              # Contains the serialized model (model.pkl)
├── src/                # Backend logic and training scripts (train_model.py)
├── static/             # Front-end styling (style.css)
├── templates/          # HTML pages (index.html, result.html)
├── app.py              # Main Flask application entry point
├── requirements.txt    # Project dependencies
└── README.md           # Documentation
