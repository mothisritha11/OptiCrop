OPTICROP🌾

OptiCrop is an intelligent, data-driven agriculture assistant designed to help farmers, agronomists, and agricultural enthusiasts optimize crop yields. By leveraging machine learning and environmental data, OptiCrop provides accurate recommendations for crop selection, fertilizer optimization, and early plant disease detection.

---

## 🚀 Features

* **Crop Recommendation:** Suggests the most optimal crop to plant based on soil composition (Nitrogen, Phosphorus, Potassium) and climatic conditions (Temperature, Humidity, pH, Rainfall).
* **Fertilizer Prediction:** Analyzes soil health and current crop requirements to recommend the exact fertilizer needed for maximum yield.
* **Plant Disease Detection:** Utilizes computer vision to identify plant diseases from images of leaves and provides actionable remedies.
* **User-Friendly Interface:** Built with an intuitive frontend ensuring ease of use for tech-savvy users and farmers alike.

---

## 🛠️ Tech Stack

* **Frontend:** HTML5, CSS3, JavaScript / Streamlit *(or Flask/React depending on your UI choice)*
* **Backend:** Python, Flask / FastAPI
* **Machine Learning / Deep Learning:** Scikit-Learn, TensorFlow / PyTorch, Pandas, NumPy
* **Deployment:** Heroku / AWS / Render *(Update based on your deployment)*
```
## Screenshots

### Home Page
![Home](assets/image1.png)

### Prediction Page
![Prediction](assets/image2.png)

### Result Output
![Result](assets/image3.png)

## 📁 Project Structure

```text
OptiCrop/
│
├── dataset/                # Dataset used for training ML models
├── models/                 # Trained .pkl or .h5 model files
├── notebooks/              # Jupyter notebooks for data analysis & model training
├── static/                 # CSS, JavaScript, and image assets
├── templates/              # HTML templates for the web app
├── app.py                  # Main application file (Flask/Streamlit entry point)
├── requirements.txt        # List of required Python packages
└── README.md               # Project documentation

```

---

## ⚙️ Installation & Setup

Follow these steps to run OptiCrop locally on your machine:

### 1. Clone the Repository

```bash
git clone https://github.com/mothisritha11/OptiCrop.git
cd OptiCrop

```

### 2. Create a Virtual Environment

It is recommended to use a virtual environment to avoid dependency conflicts.

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate

```

### 3. Install Dependencies

```bash
pip install -r requirements.txt

```

### 4. Run the Application

```bash
# For Flask application
python app.py

# For Streamlit application (if applicable)
streamlit run app.py

```

Open your web browser and navigate to `[http://127.0.0.1:5000](http://127.0.0.1:5000)` (or the port specified in your terminal) to view the app.

---

## 🧠 Machine Learning Overview

* **Crop Prediction:** Trained using classification algorithms like **Random Forest / XGBoost**, achieving high accuracy by mapping N-P-K values and weather parameters to ideal crops.
* **Disease Detection:** Uses **Convolutional Neural Networks (CNN)** trained on plant village datasets to classify healthy vs. diseased leaves.

---

## 🤝 Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---

## 📞 Contact

**Mothisritha** - [@mothisritha11](https://www.google.com/search?q=https://github.com/mothisritha11)

Project Link: [https://github.com/mothisritha11/OptiCrop](https://github.com/mothisritha11/OptiCrop)

---

