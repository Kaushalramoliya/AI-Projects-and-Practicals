'''  
@author: 22000409 Kaushal Ramoliya  
@description: 24.1. -  Regression using KNN, Linear, Ridge, Lasso and ElasticNet on cars.csv dataset to predict 
CO2 emission. 
'''  
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error, r2_score

# Load dataset
cars = pd.read_csv('Program_24.1_cars.csv')  # Update path if needed

# Display columns to verify
print("Columns in dataset:", cars.columns.tolist())

# Select features and target
X = cars[['Volume', 'Weight']]
y = cars['CO2']

# Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Dictionary to store results
results = {}

# Define and evaluate models
models = {
    "KNN": KNeighborsRegressor(n_neighbors=5),
    "LinearRegression": LinearRegression(),
    "Ridge": Ridge(alpha=1.0),
    "Lasso": Lasso(alpha=0.1),
    "ElasticNet": ElasticNet(alpha=0.1, l1_ratio=0.5)
}

# Train, predict and calculate metrics
for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    results[name] = {"MSE": round(mse, 2), "R2_Score": round(r2, 4)}

# Display the results
print("\n--- Regression Results ---")
print("{:<15} {:<10} {:<10}".format("Model", "MSE", "R2 Score"))
print("-" * 35)
for model, metrics in results.items():
    print(f"{model:<15} {metrics['MSE']:<10} {metrics['R2_Score']:<10}")
