import pandas as pd
import matplotlib.pyplot as plt
data = {
    'customer_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'customer_age': [25, 30, 22, 30, 25, 22, 35, 30, 40, 22],
    'purchase_amount': [450, 700, 300, 800, 450, 600, 1200, 450, 1200, 300]
}
sales_data = pd.DataFrame(data)
age_distribution = sales_data['customer_age'].value_counts().sort_index()
print("📊 Frequency Distribution of Customer Ages:\n")
print(age_distribution)
purchase_distribution = sales_data['purchase_amount'].value_counts().sort_index()
print("\n💰 Frequency Distribution of Purchase Amounts:\n")
print(purchase_distribution)
plt.figure(figsize=(14, 5))
plt.subplot(1, 2, 1)
age_distribution.plot(kind='bar', color='steelblue', edgecolor='black')
plt.title("Frequency of Customer Ages")
plt.xlabel("Age")
plt.ylabel("Number of Customers")
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.subplot(1, 2, 2)
purchase_distribution.plot(kind='bar', color='darkorange', edgecolor='black')
plt.title("Frequency of Purchase Amounts")
plt.xlabel("Purchase Amount (₹)")
plt.ylabel("Number of Purchases")
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()