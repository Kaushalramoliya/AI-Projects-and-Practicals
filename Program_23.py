'''  
@author: 22000409 Kaushal Ramoliya  
@description: 23. -  Write a python script to implement 
1. KNN Classifier and 
2. KNN Regression  
'''  
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.metrics import accuracy_score, mean_squared_error

# Load datasets
user_data = pd.read_csv('Program_23_user_data_cars_1.csv')
pima = pd.read_csv('Program_23_pima-indians-diabetes.csv')
cars = pd.read_csv('Program_23cars.csv')

# Clean pima dataset
pima.columns = pima.iloc[0]  # Use the first row as column headers
pima = pima[1:].reset_index(drop=True)
pima = pima.apply(pd.to_numeric, errors='coerce').dropna()


# Encode 'Gender' in user data
user_data["Gender"] = LabelEncoder().fit_transform(user_data["Gender"])

# Features and targets
X_user = user_data[["Gender", "Age", "EstimatedSalary"]]
y_user = user_data["Purchased"]

X_pima = pima.drop(columns=["class"])
y_pima = pima["class"]

X_cars = cars[["Volume", "Weight"]]
y_cars = cars["CO2"]

# Standardize features
scaler = StandardScaler()
X_user = scaler.fit_transform(X_user)
X_pima = scaler.fit_transform(X_pima)
X_cars = scaler.fit_transform(X_cars)

# Train-Test Split
X_user_train, X_user_test, y_user_train, y_user_test = train_test_split(X_user, y_user, test_size=0.2, random_state=42)
X_pima_train, X_pima_test, y_pima_train, y_pima_test = train_test_split(X_pima, y_pima, test_size=0.2, random_state=42)
X_cars_train, X_cars_test, y_cars_train, y_cars_test = train_test_split(X_cars, y_cars, test_size=0.2, random_state=42)

# Record results
results = {"K": [], "UserData_Accuracy (%)": [], "Pima_Accuracy (%)": [], "Cars_MSE": []}

# --- KNN Loop ---
for k in range(1, 11):
    # User Data - Classification
    knn_user = KNeighborsClassifier(n_neighbors=k)
    knn_user.fit(X_user_train, y_user_train)
    pred_user = knn_user.predict(X_user_test)
    acc_user = accuracy_score(y_user_test, pred_user) * 100

    # Pima Data - Classification
    knn_pima = KNeighborsClassifier(n_neighbors=k)
    knn_pima.fit(X_pima_train, y_pima_train)
    pred_pima = knn_pima.predict(X_pima_test)
    acc_pima = accuracy_score(y_pima_test, pred_pima) * 100

    # Cars Data - Regression
    knn_cars = KNeighborsRegressor(n_neighbors=k)
    knn_cars.fit(X_cars_train, y_cars_train)
    pred_cars = knn_cars.predict(X_cars_test)
    mse_cars = mean_squared_error(y_cars_test, pred_cars)

    # Save results
    results["K"].append(k)
    results["UserData_Accuracy (%)"].append(round(acc_user, 2))
    results["Pima_Accuracy (%)"].append(round(acc_pima, 2))
    results["Cars_MSE"].append(round(mse_cars, 2))

# Save to CSV
results_df = pd.DataFrame(results)
results_df.to_csv("Program_23_KNN_Results.csv", index=False)

# Show the final result
print("KNN Evaluation Completed. Results:")
print(results_df)
