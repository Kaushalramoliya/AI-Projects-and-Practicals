'''  
@author: 22000409 Kaushal Ramoliya  
@description: 22.1 -  Create a model to predict whether a person will have car or not based on dataset attached using Naive Bayes Classifier. (user_data_cars_1.csv)  
'''  
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load the dataset
df = pd.read_csv("Program_22.1_user_data_cars_1.csv")

# Drop the 'User ID' column as it's not useful for prediction
df = df.drop("User ID", axis=1)

# Encode the 'Gender' column (Male/Female -> 1/0)
le_gender = LabelEncoder()
df["Gender"] = le_gender.fit_transform(df["Gender"])

# Define features and target
X = df[["Gender", "Age", "EstimatedSalary"]]
y = df["Purchased"]

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the Gaussian Naive Bayes model
model = GaussianNB()
model.fit(X_train, y_train)

# Predict on test data
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")
print("\nClassification Report:\n", classification_report(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))

# Example prediction
# Example input: Female, Age 30, EstimatedSalary 60000
sample_input = pd.DataFrame({
    "Gender": le_gender.transform(["Female"]),
    "Age": [30],
    "EstimatedSalary": [60000]
})

sample_prediction = model.predict(sample_input)

if sample_prediction[0] == 1:
    print("\nPrediction: The person is likely to purchase a car.")
else:
    print("\nPrediction: The person is not likely to purchase a car.")

