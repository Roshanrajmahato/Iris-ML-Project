# train_model.py
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
import os
import pandas as pd


# Load iris
data = load_iris()
X = data.data
y = data.target


# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# Train model
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)


# Evaluate
pred = clf.predict(X_test)
acc = accuracy_score(y_test, pred)
print(f"Test accuracy: {acc:.4f}")


# Save model
os.makedirs('model', exist_ok=True)
joblib.dump(clf, 'model/iris_model.pkl')
print('Saved model to model/iris_model.pkl')