'''  
@author: 22000409 Kaushal Ramoliya  
@description: 22.4 -  Write python script to implement Random Forest classifier on following dataset. 
(iris.csv) 
'''  
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# 1. Load dataset
df = pd.read_csv("Program_22.4_iris.csv")

# 2. Show column names to identify target
print("Columns in the dataset:")
print(df.columns)

# Let's assume the last column is the target (usually correct for iris datasets)
X = df.iloc[:, :-1]
y = df.iloc[:, -1]

# 3. Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Initialize and train the Random Forest Classifier
rfc = RandomForestClassifier(n_estimators=4, random_state=42)
rfc.fit(X_train, y_train)

# 5. Predict
y_pred = rfc.predict(X_test)

# 6. Evaluation
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("Accuracy Score:", accuracy_score(y_test, y_pred))
