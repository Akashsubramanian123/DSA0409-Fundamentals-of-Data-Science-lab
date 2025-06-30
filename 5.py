import numpy as np
fuel_efficiency = np.array([20, 22, 25, 30, 28, 35, 33])
car_models = np.array(['Model A', 'Model B', 'Model C', 'Model D', 'Model E', 'Model F', 'Model G'])
average_efficiency = np.mean(fuel_efficiency)
model_a_eff = fuel_efficiency[0]
model_b_eff = fuel_efficiency[5]
percentage_improvement = ((model_b_eff - model_a_eff) / model_a_eff) * 100
max_efficiency = np.max(fuel_efficiency)
max_index = np.argmax(fuel_efficiency)
most_efficient_model = car_models[max_index]
print("Fuel Efficiency Data (MPG):")
for name, mpg in zip(car_models, fuel_efficiency):
    print(f"{name}: {mpg} MPG")
print(f"\nAverage Fuel Efficiency: {average_efficiency:.2f} MPG")
print(f"Percentage Improvement from Model A to Model F: {percentage_improvement:.2f}%")
print(f"Most Fuel Efficient Model: {most_efficient_model} ({max_efficiency} MPG)")