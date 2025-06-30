import pandas as pd

# 1. Load dataset
df = pd.read_csv("temperature_data.csv", parse_dates=["Date"])

# 2. Group by city and calculate required metrics
city_stats = df.groupby('City')['Temperature'].agg(
    Mean_Temp='mean',
    Std_Dev='std',
    Max_Temp='max',
    Min_Temp='min'
)

# 3. Add Temperature Range
city_stats['Temp_Range'] = city_stats['Max_Temp'] - city_stats['Min_Temp']

# 4. Identify key insights
most_variable_city = city_stats['Temp_Range'].idxmax()
most_consistent_city = city_stats['Std_Dev'].idxmin()

# 5. Display results
print("\n📊 Temperature Summary by City:")
print(city_stats[['Mean_Temp', 'Std_Dev', 'Temp_Range']])

print(f"\n🔥 City with Highest Temperature Range: {most_variable_city} ({city_stats.loc[most_variable_city, 'Temp_Range']:.2f}°C)")
print(f"❄️ City with Most Consistent Temperature: {most_consistent_city} (Std Dev: {city_stats.loc[most_consistent_city, 'Std_Dev']:.2f}°C)")
