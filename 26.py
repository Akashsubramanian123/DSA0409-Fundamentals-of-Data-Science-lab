import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
X = np.array([
    [1200, 2, 0],
    [1500, 3, 1],
    [800, 1, 2],
    [2000, 4, 1],
    [950, 2, 2],
    [1750, 3, 0],
    [1400, 3, 1],
    [2200, 4, 0],
    [1600, 2, 1],
    [1300, 2, 2]
])
y = np.array([300000, 500000, 180000, 650000, 200000, 450000, 480000, 700000, 520000, 250000])
model = LinearRegression()
model.fit(X, y)
try:
    print("\n🏠 Enter details of the house:")
    area = float(input("Area (sq ft): "))
    bedrooms = int(input("Number of bedrooms: "))
    print("Location options: 0 = Suburb, 1 = City, 2 = Rural")
    location_code = int(input("Location code: "))
    features = [[area, bedrooms, location_code]]
except:
    print("❌ Invalid input.")
    exit()
predicted_price = model.predict(features)[0]
print(f"\n💰 Predicted House Price: ₹{predicted_price:,.2f}")