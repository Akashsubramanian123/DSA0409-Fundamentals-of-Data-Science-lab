from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
iris = load_iris()
X = iris.data
y = iris.target
species_names = iris.target_names
model = DecisionTreeClassifier(random_state=0)
model.fit(X, y)
try:
    print("\n🌼 Enter the features of the Iris flower:")
    sepal_length = float(input("Sepal length (cm): "))
    sepal_width = float(input("Sepal width (cm): "))
    petal_length = float(input("Petal length (cm): "))
    petal_width = float(input("Petal width (cm): "))
    features = [[sepal_length, sepal_width, petal_length, petal_width]]
except:
    print("❌ Invalid input. Please enter numeric values.")
    exit()
prediction = model.predict(features)[0]
predicted_species = species_names[prediction]
print(f"\n🔍 Predicted Species: {predicted_species.capitalize()}")