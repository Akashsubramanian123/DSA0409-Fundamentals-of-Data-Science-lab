import numpy as np

# Sample house data: [Bedrooms, Square Footage, Sale Price]
house_data = np.array([
    [3, 1500, 250000],
    [5, 2400, 400000],
    [4, 2000, 350000],
    [6, 3000, 520000],
    [5, 2800, 450000],
    [2, 1200, 180000]
])

# Step 1: Filter rows where bedrooms > 4
filter_mask = house_data[:, 0] > 4
filtered_houses = house_data[filter_mask]

# Step 2: Extract square footage and sale prices
filtered_square_footage = filtered_houses[:, 1]
filtered_sale_prices = filtered_houses[:, 2]

# Step 3: Calculate averages
average_price = np.mean(filtered_sale_prices)
average_sqft = np.mean(filtered_square_footage)

# Output results
print("Filtered Houses (Bedrooms > 4):\n", filtered_houses)
print(f"\nAverage Sale Price: ₹{average_price:,.2f}")
print(f"Average Square Footage: {average_sqft:.2f} sq.ft")
