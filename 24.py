import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification
X, y = make_classification(n_samples=100, n_features=4, n_classes=2,
                           n_informative=3, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
try:
    print("\n🔍 Enter symptom values for the new patient:")
    symptoms = [float(input(f"Symptom {i+1}: ")) for i in range(X.shape[1])]
    k = int(input("Enter the value of k (number of neighbors): "))
except:
    print("❌ Invalid input.")
    exit()
model = KNeighborsClassifier(n_neighbors=k)
model.fit(X_train, y_train)
prediction = model.predict([symptoms])[0]
print("\n📊 Prediction Result:")
print("✅ The patient **has the condition**." if prediction == 1 else "❎ The patient **does NOT have the condition**.")