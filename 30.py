import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeRegressor, export_text
from sklearn.preprocessing import LabelEncoder

# 1. Simulated car dataset
data = {
    "mileage": [10, 15, 20, 25, 18, 12, 30, 22, 14, 16],
    "age": [5, 3, 2, 1, 4, 6, 1, 3, 7, 2],
    "brand": ["Toyota", "Honda", "Hyundai", "Toyota", "Hyundai", "Honda", "Hyundai", "Toyota", "Honda", "Hyundai"],
    "engine_type": ["Petrol", "Diesel", "Diesel", "Electric", "Petrol", "Diesel", "Electric", "Petrol", "Diesel", "Electric"],
    "price": [400000, 450000, 500000, 700000, 480000, 350000, 750000, 420000, 300000, 720000]
}

df = pd.DataFrame(data)

# 2. Encode categorical features
le_brand = LabelEncoder()
le_engine = LabelEncoder()
df['brand_encoded'] = le_brand.fit_transform(df['brand'])
df['engine_encoded'] = le_engine.fit_transform(df['engine_type'])

# 3. Features and target
X = df[['mileage', 'age', 'brand_encoded', 'engine_encoded']]
y = df['price']

# 4. Train CART model
model = DecisionTreeRegressor(random_state=42)
model.fit(X, y)

# 5. Take new user input
try:
    print("\n🚘 Enter details of the car to estimate its price:")
    mileage = float(input("Mileage (km/l or km driven): "))
    age = int(input("Age (in years): "))
    brand = input(f"Brand ({', '.join(le_brand.classes_)}): ").strip()
    engine_type = input(f"Engine Type ({', '.join(le_engine.classes_)}): ").strip()

    # Encode user input
    brand_encoded = le_brand.transform([brand])[0]
    engine_encoded = le_engine.transform([engine_type])[0]
    new_car = np.array([[mileage, age, brand_encoded, engine_encoded]])
except Exception as e:
    print("❌ Invalid input:", e)
    exit()

# 6. Predict price
predicted_price = model.predict(new_car)[0]
print(f"\n💰 Predicted Price: ₹{predicted_price:,.2f}")

# 7. Show decision path
print("\n🌳 Decision Path Explanation:")
tree_rules = export_text(model, feature_names=['mileage', 'age', 'brand_encoded', 'engine_encoded'])
print(tree_rules)
