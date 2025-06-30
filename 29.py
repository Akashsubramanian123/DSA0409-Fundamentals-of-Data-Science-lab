import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report

# 1. Load dataset
data = load_breast_cancer()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target

print("\n📊 Available columns:")
print(df.columns.tolist())

# 2. User inputs
target_col = input("\nEnter the name of the target variable: ").strip()
feature_cols = input("Enter feature columns (comma-separated): ").strip().split(",")

# Clean column names
feature_cols = [col.strip() for col in feature_cols]

# 3. Prepare data
try:
    X = df[feature_cols]
    y = df[target_col]
except KeyError:
    print("❌ Invalid column names.")
    exit()

# 4. Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 5. Train model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# 6. Predict
y_pred = model.predict(X_test)

# 7. Evaluation Metrics
print("\n✅ Model Evaluation:")
print(f"Accuracy  : {accuracy_score(y_test, y_pred):.4f}")
print(f"Precision : {precision_score(y_test, y_pred):.4f}")
print(f"Recall    : {recall_score(y_test, y_pred):.4f}")
print(f"F1 Score  : {f1_score(y_test, y_pred):.4f}")
print("\nDetailed Report:\n")
print(classification_report(y_test, y_pred, target_names=data.target_names))
