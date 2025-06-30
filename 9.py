import pandas as pd
import matplotlib.pyplot as plt
data = {
    'property_id': [101, 102, 103, 104, 105, 106],
    'location': ['Downtown', 'Uptown', 'Downtown', 'Suburb', 'Uptown', 'Suburb'],
    'bedrooms': [3, 5, 4, 2, 6, 5],
    'area_sqft': [1200, 2500, 1500, 900, 3000, 2800],
    'listing_price': [5000000, 9000000, 6000000, 3500000, 12000000, 11000000]
}
property_data = pd.DataFrame(data)
avg_price_by_location = property_data.groupby('location')['listing_price'].mean()
print("1. Average Listing Price per Location:\n", avg_price_by_location, "\n")
more_than_4_bed = property_data[property_data['bedrooms'] > 4].shape[0]
print("2. Number of Properties with More Than 4 Bedrooms:", more_than_4_bed, "\n")
largest_area_index = property_data['area_sqft'].idxmax()
largest_property = property_data.loc[largest_area_index]
print("3. Property with the Largest Area:\n", largest_property)
plt.figure(figsize=(8, 5))
avg_price_by_location.plot(kind='bar', color='teal', edgecolor='black')
plt.title("Average Listing Price by Location")
plt.xlabel("Location")
plt.ylabel("Average Price (₹)")
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()