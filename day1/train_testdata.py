# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 17:16:02 2023

@author: Balasubramaniam
"""

import pandas as pd

df =pd.read_csv("F:/verizonmldec2023/datasets/Data.csv")

# select all rows and all the columns except last column

X=df.iloc[:,:-1].values

print(X)

## select all the rows and last column 
Y=df.iloc[:,-1].values
print(Y)

#split the data into training data and test data

from sklearn.model_selection import train_test_split
 
X_Train, X_Test, Y_Train,Y_Test=train_test_split(X,Y,test_size=0.30,random_state=0 )

print("X Training Data.............")
print(X_Train)

print("X Test Data.............")
print(X_Test)

print("Y Training Data.............")
print(Y_Train)

print("Y Test Data.............")
print(Y_Test)

#categorical data encoding
# preprocessing
from sklearn.preprocessing import LabelEncoder

labelEncoder=LabelEncoder()

X[:,0]=labelEncoder.fit_transform(X[:,0])
print(X)

Y=labelEncoder.fit_transform(Y)
print(Y)