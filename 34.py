import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report

# 1. Simulate patient dataset
np.random.seed(42)
n_samples = 200

df = pd.DataFrame({
    'age': np.random.randint(30, 80, n_samples),
    'gender': np.random.choice(['Male', 'Female'], n_samples),
    'blood_pressure': np.random.randint(110, 180, n_samples),
    'cholesterol': np.random.randint(150, 300, n_samples),
    'outcome': np.random.choice(['Good', 'Bad'], n_samples, p=[0.6, 0.4])
})

# 2. Encode categorical data
le_gender = LabelEncoder()
le_outcome = LabelEncoder()
df['gender_encoded'] = le_gender.fit_transform(df['gender'])
df['outcome_encoded'] = le_outcome.fit_transform(df['outcome'])  # Good=1, Bad=0

# 3. Define features and target
X = df[['age', 'gender_encoded', 'blood_pressure', 'cholesterol']]
y = df['outcome_encoded']

# 4. Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 5. Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

# 6. Train KNN classifier
k = 5
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(X_train, y_train)

# 7. Predict and evaluate
y_pred = knn.predict(X_test)

print("\n🔍 Classification Metrics:")
print(f"Accuracy : {accuracy_score(y_test, y_pred):.4f}")
print(f"Precision: {precision_score(y_test, y_pred):.4f}")
print(f"Recall   : {recall_score(y_test, y_pred):.4f}")
print(f"F1-score : {f1_score(y_test, y_pred):.4f}")
print("\nDetailed Classification Report:\n")
print(classification_report(y_test, y_pred, target_names=['Bad', 'Good']))

# 8. (Optional) Show a few predictions
results_df = pd.DataFrame(X_test, columns=['age', 'gender_encoded', 'blood_pressure', 'cholesterol'])
results_df['Actual'] = le_outcome.inverse_transform(y_test)
results_df['Predicted'] = le_outcome.inverse_transform(y_pred)
print("\n📋 Sample Predictions:\n")
print(results_df.head(10))
