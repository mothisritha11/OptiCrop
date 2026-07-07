import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load dataset
df = pd.read_csv("dataset/Crop_recommendation.csv")

# Features & Target
X = df.drop("label", axis=1)
y = df["label"]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Calculate and print Accuracy
accuracy = model.score(X_test, y_test)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

# Save the trained model
# Note: Use "model/model.pkl" if you want it inside a 'model' subfolder
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved successfully as model.pkl!")