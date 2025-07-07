'''  
@author: 22000409 Kaushal Ramoliya  
@description: 20. -  Naive Bayes classification using python sklearns lib for below given tabular data.
'''  
import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.naive_bayes import BernoulliNB

df = pd.read_excel("Program_20_excel.xlsx")


X = df.iloc[:, 1:-1]  # Color, Type, Origin)
y = df.iloc[:, -1]   # (Stolen)

# Encoding categorical variables
le_color = preprocessing.LabelEncoder()
le_type = preprocessing.LabelEncoder()
le_origin = preprocessing.LabelEncoder()
le_stolen = preprocessing.LabelEncoder()

X['Color'] = le_color.fit_transform(X['Color'])
X['Type'] = le_type.fit_transform(X['Type'])
X['Origin'] = le_origin.fit_transform(X['Origin'])
y = le_stolen.fit_transform(y)

features = np.array(list(zip(X['Color'], X['Type'], X['Origin'])))

# Train the model
model = BernoulliNB()
model.fit(features, y)


# Test the model with a sample input
test_data = np.array([['Yellow', 'Sports', 'Imported']])
test_data[:, 0] = le_color.fit_transform(test_data[:, 0])
test_data[:, 1] = le_type.fit_transform(test_data[:, 1])
test_data[:, 2] = le_origin.fit_transform(test_data[:, 2])
test_data = test_data.astype(int)

# Predict the outcome
predicted = model.predict(test_data)


if predicted[0] == 0:
    print("Car is not stolen")
else:
    print("Car is stolen")
