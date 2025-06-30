import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# 1. Simulated dataset
np.random.seed(42)
size = np.random.normal(1500, 300, 100)  # size in sq ft
price = size * 300 + np.random.normal(0, 50000, 100)  # price with noise

df = pd.DataFrame({'size': size, 'price': price})

# 2. Bivariate analysis: scatter plot
plt.figure(figsize=(8, 5))
plt.scatter(df['size'], df['price'], alpha=0.7, edgecolor='k')
plt.title("Bivariate Analysis: Size vs Price")
plt.xlabel("Size (sq ft)")
plt.ylabel("Price (₹)")
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

# 3. Linear regression model
X = df[['size']]
y = df['price']

model = LinearRegression()
model.fit(X, y)

# 4. Predictions
y_pred = model.predict(X)

# 5. Evaluation
mae = mean_absolute_error(y, y_pred)
rmse = np.sqrt(mean_squared_error(y, y_pred))
r2 = r2_score(y, y_pred)

print("\n📊 Model Evaluation:")
print(f"Intercept: {model.intercept_:.2f}")
print(f"Slope (coef): {model.coef_[0]:.2f}")
print(f"R² Score: {r2:.4f}")
print(f"MAE: ₹{mae:,.2f}")
print(f"RMSE: ₹{rmse:,.2f}")

# 6. Plot regression line
plt.figure(figsize=(8, 5))
plt.scatter(X, y, label='Actual', alpha=0.7, edgecolor='k')
plt.plot(X, y_pred, color='red', label='Regression Line')
plt.title("Linear Regression: Size vs Price")
plt.xlabel("Size (sq ft)")
plt.ylabel("Price (₹)")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

# 7. Residual Plot
residuals = y - y_pred
plt.figure(figsize=(8, 4))
plt.scatter(y_pred, residuals, alpha=0.7)
plt.axhline(0, color='red', linestyle='--')
plt.title("Residual Plot")
plt.xlabel("Predicted Price (₹)")
plt.ylabel("Residuals")
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()
