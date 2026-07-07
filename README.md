# 🌱 OptiCrop – Smart Crop Recommendation System

## 📌 Overview

OptiCrop is a Machine Learning-based web application that recommends the most suitable crop to grow based on environmental and soil conditions. The system helps farmers and agricultural planners make data-driven decisions to improve productivity and sustainability.

---

## 🚀 Features

* 🌾 Predicts best crop based on input parameters
* 📊 Uses Machine Learning for accurate recommendations
* 🌐 Simple and user-friendly web interface
* ⚡ Fast and real-time predictions
* 📁 Organized project structure

---

## 🛠️ Tech Stack

* **Programming Language:** Python
* **Framework:** Flask
* **Libraries:**

  * Pandas
  * NumPy
  * Scikit-learn
* **Frontend:** HTML, CSS
* **Model Storage:** Pickle (`.pkl` file)

---

## 📂 Project Structure

```
OptiCrop/
│── dataset/              # Dataset used for training
│── model/                # Saved ML model (model.pkl)
│── static/               # CSS, JS, images
│── templates/            # HTML files
│── src/                  # Source code files
│── app.py                # Main Flask application
│── requirements.txt      # Dependencies
│── README.md             # Project documentation
```
## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```
git clone https://github.com/mothisritha11/OptiCrop.git
cd OptiCrop
```

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Run the Application

```
python app.py
```

### 4️⃣ Open in Browser

```
http://127.0.0.1:5000/
```

---

## 🤖 Machine Learning Model

The model is trained using agricultural data including:

* Nitrogen (N)
* Phosphorus (P)
* Potassium (K)
* Temperature
* Humidity
* pH value
* Rainfall

The trained model is saved as:

```
model/model.pkl
```

---

## 📸 Screenshots

*(Add your project screenshots here for better presentation)*

---

## 📈 Future Enhancements

* 📱 Mobile-friendly UI
* 🌍 Weather API integration
* 📊 Advanced analytics dashboard
* 🌱 Fertilizer recommendation system

---

## 👩‍💻 Author

**Mothi Sritha**

---

## 📜 License

This project is open-source and available under the MIT License.

---

## ⭐ Acknowledgements

* Scikit-learn Documentation
* Open-source datasets for agriculture
