import pandas as pd
df = pd.read_csv("employee_data.csv")
df['Salary'] = pd.to_numeric(df['Salary'].replace(r'[\$,]', '', regex=True))
df=df.dropna(subset=['Department'])
df['First Name'] = df['Full Name'].str.split().str[0]
print(df)