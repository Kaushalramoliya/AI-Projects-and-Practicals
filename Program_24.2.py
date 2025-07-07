'''  
@author: 22000409 Kaushal Ramoliya  
@description: 24.2. -  Classification using LogisticRegression on pima-indiana-diabetes.csv. 
'''  
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Load dataset
pima = pd.read_csv('Program_24.2_pima-indians-diabetes.csv')

# Display columns and first few rows
print("Columns in dataset:", pima.columns.tolist())
print(pima.head())

# Clean dataset (if needed: sometimes first row might be column headers in disguised form)
if not pd.api.types.is_numeric_dtype(pima.iloc[0, 0]):
    pima.columns = pima.iloc[0]
    pima = pima[1:].reset_index(drop=True)

# Convert all to numeric and drop NaNs
pima = pima.apply(pd.to_numeric, errors='coerce').dropna()

# Features and target
X = pima.drop(columns=["class"])
y = pima["class"]

# Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Logistic Regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
acc = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)
report = classification_report(y_test, y_pred)

# Print results
print("\n--- Logistic Regression Results ---")
print(f"Accuracy: {acc * 100:.2f}%")
print("\nConfusion Matrix:")
print(cm)
print("\nClassification Report:")
print(report)