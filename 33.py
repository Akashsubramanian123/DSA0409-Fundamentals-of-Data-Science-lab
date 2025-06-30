import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Simulated dataset
np.random.seed(42)
df = pd.DataFrame({
    'engine_size': np.random.uniform(1.0, 5.0, 100),
    'horsepower': np.random.randint(70, 300, 100),
    'fuel_efficiency': np.random.uniform(8, 22, 100)
})

# Price influenced by these features + some noise
df['price'] = (
    df['engine_size'] * 300000 +
    df['horsepower'] * 1000 -
    df['fuel_efficiency'] * 5000 +
    np.random.normal(0, 50000, 100)
)

# 2. Exploratory Plot
sns.pairplot(df)
plt.suptitle("Car Features vs Price", y=1.02)
plt.show()

# 3. Features and Target
X = df[['engine_size', 'horsepower', 'fuel_efficiency']]
y = df['price']

# 4. Fit Linear Regression Model
model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)

# 5. Evaluation Metrics
r2 = r2_score(y, y_pred)
mae = mean_absolute_error(y, y_pred)
rmse = np.sqrt(mean_squared_error(y, y_pred))

print("\n📊 Model Performance Metrics:")
print(f"R² Score       : {r2:.4f}")
print(f"Mean Absolute Error (MAE): ₹{mae:,.2f}")
print(f"Root Mean Squared Error (RMSE): ₹{rmse:,.2f}")

# 6. Coefficients: Insights for Marketing Team
print("\n💡 Feature Influence on Price (Model Coefficients):")
coef_df = pd.DataFrame({
    'Feature': X.columns,
    'Coefficient': model.coef_
})
print(coef_df)

# 7. Plot: Actual vs Predicted
plt.figure(figsize=(7, 5))
plt.scatter(y, y_pred, alpha=0.7)
plt.plot([y.min(), y.max()], [y.min(), y.max()], color='red', linestyle='--')
plt.xlabel("Actual Price (₹)")
plt.ylabel("Predicted Price (₹)")
plt.title("Actual vs Predicted Car Prices")
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()
