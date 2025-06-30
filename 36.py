import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load data
df = pd.read_csv("stock_data.csv", parse_dates=["Date"])
df.sort_values("Date", inplace=True)

# 2. Calculate daily returns
df['Daily Return (%)'] = df['Close'].pct_change() * 100

# 3. Variability metrics
std_dev = df['Close'].std()
volatility = df['Daily Return (%)'].std()
mean_return = df['Daily Return (%)'].mean()

print("\n📈 Stock Price Variability Insights:")
print(f"Standard Deviation of Closing Price: ₹{std_dev:.2f}")
print(f"Mean Daily Return: {mean_return:.2f}%")
print(f"Volatility (Std Dev of Daily Return): {volatility:.2f}%")

# 4. Plot closing price
plt.figure(figsize=(10, 5))
plt.plot(df['Date'], df['Close'], marker='o', linewidth=1.5)
plt.title("Closing Price Over Time")
plt.xlabel("Date")
plt.ylabel("Closing Price (₹)")
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

# 5. Plot return distribution
plt.figure(figsize=(8, 5))
sns.histplot(df['Daily Return (%)'].dropna(), bins=30, kde=True, color='skyblue')
plt.axvline(mean_return, color='green', linestyle='--', label=f'Mean: {mean_return:.2f}%')
plt.axvline(mean_return + volatility, color='red', linestyle='--', label='+1 Std Dev')
plt.axvline(mean_return - volatility, color='red', linestyle='--', label='-1 Std Dev')
plt.title("Daily Return Distribution")
plt.xlabel("Daily Return (%)")
plt.ylabel("Frequency")
plt.legend()
plt.tight_layout()
plt.show()
