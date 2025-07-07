'''  
@author: 22000409 Kaushal Ramoliya  
@description: 26. -   Develop a ML model to predict car price from the given dataset (usedcars.csv)
'''  
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error, r2_score

# Load your dataset (example using a CSV file)
df = pd.read_csv('Program_26_usedcars.csv')

# Display the shape
print("Shape of the dataset:", df.shape)  # (rows, columns)

# Display the column names
print("Columns in the dataset:")
print(df.columns)

# Check for null values in each column
print("Null values in each column:")
print(df.isnull().sum())

# Show descriptive statistics
print("Descriptive statistics:")
print(df.describe())

# Display unique values for each column
for column in df.columns:
    print(f"\nUnique values in '{column}':")
    print(df[column].unique())

# Perform one-hot encoding on categorical features
encoder = OneHotEncoder(sparse_output=False, drop='first')  # Use sparse_output instead of sparse
categorical_cols = df.select_dtypes(include=['object']).columns
encoded_features = encoder.fit_transform(df[categorical_cols])

# Combine numerical features and encoded categorical features
numerical_cols = df.select_dtypes(include=['number']).columns
encoded_df = pd.DataFrame(encoded_features, columns=encoder.get_feature_names_out(categorical_cols))
df_clean = pd.concat([df[numerical_cols].reset_index(drop=True), encoded_df.reset_index(drop=True)], axis=1)

# Replace 'target_column' with the actual target column name in your dataset
X = df_clean.drop(columns=['price'])  
y = df_clean['price']  

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Dictionary to store model performance
model_performance = {}

# 1. K-Nearest Neighbors Regressor (KNNR)
knn = KNeighborsRegressor(n_neighbors=10)
knn.fit(X_train, y_train)
knn_pred = knn.predict(X_test)
knn_mse = mean_squared_error(y_test, knn_pred)
knn_r2 = r2_score(y_test, knn_pred)
model_performance['KNNR'] = (knn_mse, knn_r2)

# 2. Linear Regression (LiR)
lr = LinearRegression()
lr.fit(X_train, y_train)
lr_pred = lr.predict(X_test)
lr_mse = mean_squared_error(y_test, lr_pred)
lr_r2 = r2_score(y_test, lr_pred)
model_performance['Linear Regression'] = (lr_mse, lr_r2)

# 3. Random Forest Regressor (RFR)
rfr = RandomForestRegressor(n_estimators=100, random_state=42)
rfr.fit(X_train, y_train)
rfr_pred = rfr.predict(X_test)
rfr_mse = mean_squared_error(y_test, rfr_pred)
rfr_r2 = r2_score(y_test, rfr_pred)
model_performance['Random Forest Regressor'] = (rfr_mse, rfr_r2)

# 4. Multi-Layer Perceptron (MLP) with different architectures
mlp_1 = MLPRegressor(hidden_layer_sizes=(5, 8, 1), max_iter=500, random_state=42)
mlp_1.fit(X_train, y_train)
mlp_1_pred = mlp_1.predict(X_test)
mlp_1_mse = mean_squared_error(y_test, mlp_1_pred)
mlp_1_r2 = r2_score(y_test, mlp_1_pred)
model_performance['MLP (5/8/1)'] = (mlp_1_mse, mlp_1_r2)

mlp_2 = MLPRegressor(hidden_layer_sizes=(5, 8, 4, 1), max_iter=500, random_state=42)
mlp_2.fit(X_train, y_train)
mlp_2_pred = mlp_2.predict(X_test)
mlp_2_mse = mean_squared_error(y_test, mlp_2_pred)
mlp_2_r2 = r2_score(y_test, mlp_2_pred)
model_performance['MLP (5/8/4/1)'] = (mlp_2_mse, mlp_2_r2)

mlp_3 = MLPRegressor(hidden_layer_sizes=(5, 8, 12, 8, 1), max_iter=500, random_state=42)
mlp_3.fit(X_train, y_train)
mlp_3_pred = mlp_3.predict(X_test)
mlp_3_mse = mean_squared_error(y_test, mlp_3_pred)
mlp_3_r2 = r2_score(y_test, mlp_3_pred)
model_performance['MLP (5/8/12/8/1)'] = (mlp_3_mse, mlp_3_r2)

# Print model comparison
print("\nModel Performance Comparison:")
for model, (mse, r2) in model_performance.items():
    print(f"{model}: Mean Squared Error = {mse:.4f}, R² = {r2:.4f}")
    
    
# Find the best model based on MSE and R²
best_model = min(model_performance.items(), key=lambda x: (x[1][0], -x[1][1]))
print(f"\nBest Model: {best_model[0]}")
print(f"Mean Squared Error = {best_model[1][0]:.4f}, R² = {best_model[1][1]:.4f}")