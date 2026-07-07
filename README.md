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
🛠️ Installation & Setup
Follow these steps to run the project locally on your machine:

1. Clone the Repository
Bash
git clone [https://github.com/mothisritha11/OptiCrop.git](https://github.com/mothisritha11/OptiCrop.git)
cd OptiCrop
2. Set Up a Virtual Environment (Recommended)
Bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
3. Install Dependencies
Bash
pip install -r requirements.txt
💻 How to Run
Retraining the Model (Optional)
If you update the dataset and want to retrain or generate a fresh model.pkl:

Bash
python src/train_model.py
Launching the Web App
To start the Flask development server:

Bash
python app.py
Once running, open your web browser and navigate to: http://127.0.0.1:5000

📊 Dataset Parameters
The system evaluates 7 crucial agricultural inputs to recommend the ideal crop:

N - Ratio of Nitrogen content in soil

P - Ratio of Phosphorous content in soil

K - Ratio of Potassium content in soil

Temperature - Temperature in °C

Humidity - Relative humidity in %

pH - pH value of the soil

Rainfall - Rainfall in mm

🛠️ Tech Stack
Front-End: HTML5, CSS3

Back-End Framework: Flask (Python)

Machine Learning: Scikit-Learn, Pandas, Pickle


### How to push this to GitHub:
1. Open your `README.md` file in VS Code.
2. Clear anything that's currently in there and paste the text above.
3. Save the file (`Ctrl + S`).
4. In your PowerShell terminal, run these commands to update GitHub:
   ```bash
   git add README.md
   git commit -m "Update README with professional project documentation"
   git push origin main
