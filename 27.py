import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# 1. Simulated dataset
# [usage_minutes, contract_duration, num_complaints, support_calls]
X = np.array([
    [300, 12, 0, 1],
    [450, 24, 1, 2],
    [100, 6, 3, 5],
    [250, 18, 0, 1],
    [120, 3, 4, 6],
    [600, 36, 0, 0],
    [200, 12, 2, 3],
    [350, 24, 1, 1],
    [180, 6, 3, 4],
    [500, 30, 0, 0]
])
y = np.array([0, 0, 1, 0, 1, 0, 1, 0, 1, 0])  # 1 = Churned, 0 = Not churned

# 2. Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

# 3. Train Logistic Regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# 4. User input
try:
    print("\n📋 Enter details for a new customer:")
    usage = float(input("Usage minutes per month: "))
    contract = int(input("Contract duration (months): "))
    complaints = int(input("Number of complaints: "))
    support_calls = int(input("Number of support calls: "))
    
    new_customer = np.array([[usage, contract, complaints, support_calls]])
except:
    print("❌ Invalid input.")
    exit()

# 5. Predict churn
prediction = model.predict(new_customer)[0]
prob = model.predict_proba(new_customer)[0][1]  # Probability of churn (class 1)

# 6. Output
print("\n🔍 Churn Prediction Result:")
print(f"Probability of churn: {prob:.2%}")
print("📌 Prediction: Customer is likely to **CHURN**." if prediction == 1 else "✅ Prediction: Customer is **NOT likely to churn**.")
