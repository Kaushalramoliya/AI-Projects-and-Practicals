'''  
@author: 22000409 Kaushal Ramoliya  
@description: 25. -  Develop a ML model to predict Quality of Milk (Low, Medium, High) from the given dataset 
(Milk_Quality.csv). 
'''  
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import zscore
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
import seaborn as sns

# 1. Read the dataset
df = pd.read_csv("Program_25_milk_quality.csv")

# Clean column names (remove extra spaces)
df.columns = df.columns.str.strip()

# Fix common typos
df = df.rename(columns={"Temprature": "Temperature"})

# 2. Display the shape of dataset
print("2. Shape of the dataset:", df.shape)

# 3. Display columns of dataset
print("Columns in the dataset:", df.columns)

# 4. Check for null values
print("Null values in each column:")
print(df.isnull().sum())

# 5. Show descriptive statistics of dataset
print(df.describe())

# 6. Display unique values in selected columns
columns = ['pH', 'Temperature']
for col in columns:
    if col in df.columns:
        print(f"\nUnique values in '{col}':")
        print(df[col].unique())
    else:
        print(f"Column '{col}' not found.")
print("-" * 40)

# 7. Z-score based outlier detection and removal
def remove_outliers_zscore(df, columns, threshold=3):
    df_cleaned = df.copy()
    for col in columns:
        if col in df_cleaned.columns:
            z_scores = zscore(df_cleaned[col])
            df_cleaned = df_cleaned[np.abs(z_scores) <= threshold]
        else:
            print(f"Column '{col}' not found for Z-score outlier detection.")
    return df_cleaned

# Columns to apply Z-score outlier removal
zscore_columns = ['pH', 'Temperature', 'Colour']
df = remove_outliers_zscore(df, zscore_columns)

# 8. Limit data to 256 rows per 'Grade' category
if 'Grade' in df.columns:
    df = df.groupby('Grade').head(256).reset_index(drop=True)
else:
    print("Column 'Grade' not found!")
    
columns = ['pH', 'Temperature', 'Colour']
for col in columns:
    if col in df.columns:
        result = np.sum(np.abs(zscore(df[col])) > 3)
        print(f"Number of outliers in '{col}' column: {result}")
    else:
        print(f"Column '{col}' not found!")

# 9. Plot all histograms in a single screen using subplots with "Normal" labels
hist_columns = ['pH', 'Temperature', 'Taste', 'Odor', 'Fat', 'Turbidity', 'Colour']
available_cols = [col for col in hist_columns if col in df.columns]

# Reference "normal" values (you can update these as per domain knowledge)
reference_values = {
    'pH': 7.0,
    'Temperature': 35.0,
    'Taste': 1.0,
    'Odor': 1.0,
    'Fat': 2.0,
    'Turbidity': 1.0,
    'Colour': 255.0
}

plt.figure(figsize=(18, 12))
for i, col in enumerate(available_cols):
    plt.subplot(3, 3, i + 1)
    df[col].plot(kind='hist', bins=30, edgecolor='black')
    plt.title(f'Histogram of {col}')
    plt.xlabel(col)
    plt.ylabel('Frequency')
    plt.grid(True)

    # Add vertical line and label for "Normal" value
    ref = reference_values.get(col, None)
    if ref is not None:
        plt.axvline(ref, color='red', linestyle='dashed', linewidth=1)
        plt.text(ref, plt.ylim()[1] * 0.9, 'Normal', color='red', fontsize=10, ha='center')

plt.tight_layout()
plt.show()

# 10. Show final count of each grade
print("\nFinal count of each Grade:")
print(df['Grade'].value_counts())

# 11. Show correlation matrix (relationship between all numerical columns)
plt.figure(figsize=(10, 8))
correlation_matrix = df.corr(numeric_only=True)

sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title("Correlation Matrix between Features")
plt.show()

# 12. Perform Scaling and Encoding
df_scaled = df.copy()

# Separate numerical and categorical columns
numerical_cols = df_scaled.select_dtypes(include=['float64', 'int64']).columns.tolist()
categorical_cols = df_scaled.select_dtypes(include=['object']).columns.tolist()

# 12.1 Scale numerical features
scaler = StandardScaler()
df_scaled[numerical_cols] = scaler.fit_transform(df_scaled[numerical_cols])

# 12.2 Encode categorical features
label_encoders = {}
for col in categorical_cols:
    le = LabelEncoder()
    df_scaled[col] = le.fit_transform(df_scaled[col])
    label_encoders[col] = le

print("\n12. Scaled and Encoded Dataset Sample:")
print(df_scaled.head())

# 13. Create and Evaluate Multiple Models
# 13.1 Prepare features and target
if 'Grade' in df_scaled.columns:
    X = df_scaled.drop('Grade', axis=1)
    y = df_scaled['Grade']
else:
    raise ValueError("Target column 'Grade' not found!")

# 13.2 Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 13.3 Define models
models = {
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "Random Forest": RandomForestClassifier(),
    "Decision Tree": DecisionTreeClassifier(),
    "K-Nearest Neighbors": KNeighborsClassifier()
}

# 13.4 Train and evaluate each model
print("\n13. Model Evaluation Results:\n")
for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"{name} Accuracy: {acc:.2f}")
    print(classification_report(y_test, y_pred, zero_division=0))
    print("-" * 50)
    
# 13.4 Train and evaluate each model
print("\n13. Model Accuracy Comparison:\n")
for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred) * 100  # Convert to percentage
    print(f"{name}: {acc:.2f}%")


