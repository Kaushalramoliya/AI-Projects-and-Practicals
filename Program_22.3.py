'''  
@author: 22000409 Kaushal Ramoliya  
@description: 22.3 -  Write a python script to implement Decision Tree classifier on same 
dataset.  (playplaynot.csv) 
'''  
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.preprocessing import LabelEncoder
    

df = pd.read_csv("Program_22.3_playplaynot.csv")


x = df.iloc[:, 0:4]
y = df.iloc[:, 4]

label_encoder = LabelEncoder() 

x.loc[:,'Weather'] = label_encoder.fit_transform(x['Weather'])
x.loc[:,'Temp'] = label_encoder.fit_transform(x['Temp'])
x.loc[:,'Humidity'] = label_encoder.fit_transform(x['Humidity'])
x.loc[:, 'Wind'] = label_encoder.fit_transform(x['Wind'])

y = label_encoder.fit_transform(y)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

clf = DecisionTreeClassifier(criterion="entropy")

clf.fit(x_train, y_train)

y_pred = clf.predict(x_test)


print("Accuracy:", metrics.accuracy_score(y_test, y_pred))

