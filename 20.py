import pandas as pd
df = pd.read_csv("customer_data.csv")
df['Spending Segment'] = df['Total Spending'].apply(
    lambda x: 'High Spenders' if x > 10000 else 'Medium Spenders' if x >= 5000 else 'Low Spenders'
)
print("Average Age by Spending Segment:\n")
print(df.groupby('Spending Segment')['Age'].mean())