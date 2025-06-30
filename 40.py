import pandas as pd
import numpy as np

# Create mock dataset
data = {
    'Name': [f'Player{i}' for i in range(1, 21)],
    'Age': np.random.randint(18, 35, size=20),
    'Position': np.random.choice(['Forward', 'Midfielder', 'Defender', 'Goalkeeper'], size=20),
    'Goals': np.random.randint(0, 30, size=20),
    'WeeklySalary': np.random.randint(20000, 150000, size=20)
}

df = pd.DataFrame(data)

# Save to CSV
df.to_csv('soccer_players.csv', index=False)
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv('soccer_players.csv')

# Top 5 goal scorers
top_goal_scorers = df.sort_values(by='Goals', ascending=False).head(5)

# Top 5 by salary
top_salary_players = df.sort_values(by='WeeklySalary', ascending=False).head(5)

# Average age
avg_age = df['Age'].mean()
above_avg_age = df[df['Age'] > avg_age]

# Position distribution
position_counts = df['Position'].value_counts()

# Print Results
print("Top 5 Goal Scorers:")
print(top_goal_scorers[['Name', 'Goals']])

print("\nTop 5 Highest Paid Players:")
print(top_salary_players[['Name', 'WeeklySalary']])

print(f"\nAverage Age: {avg_age:.2f}")
print("Players Above Average Age:")
print(above_avg_age[['Name', 'Age']])
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x='Position', palette='Set2', order=position_counts.index)
plt.title('Player Distribution by Position')
plt.xlabel('Position')
plt.ylabel('Number of Players')
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
