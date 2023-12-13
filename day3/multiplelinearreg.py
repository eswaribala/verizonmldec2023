# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 14:32:32 2023

@author: Balasubramaniam
"""

# Multiple Linear Regression

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('F:/verizonmldec2023/datasets/SalaryMulti.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 4].values

# Encoding categorical data

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)
"""
# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)

print(X_train)

"""
# Fitting Multiple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the Test set results
y_pred = regressor.predict(X_test)

print(y_pred)

# import statsmodels.api as sm

# est = sm.OLS(y_train, X_train) #ordinary least square method 
# est2 = est.fit()
# print("Summary.....")
# print(est2.summary())



#Training Instance


plt.figure()
plt.title('Total Experience vs Salary')
plt.xlabel('Total Experience')
plt.ylabel('Salary')
plt.scatter(dataset["Total Experience"].head(n=50), dataset["Salary"].head(n=50),color="blue") #color code is k or m or etc.,
#plt.scatter(x, y, color='g')
#plt.axis([0, 25, 0, 25])
plt.grid(True)
plt.show()
plt.figure()
plt.title('Team Lead Experience vs Salary')
plt.xlabel('Team Lead Experience')
plt.ylabel('Salary')
plt.scatter(dataset["Team Lead Experience"].head(n=50), dataset["Salary"].head(n=50), color="green") #color code is k or m or etc.,
#plt.axis([0, 25, 0, 25])
plt.grid(True)
plt.show()
plt.figure()
plt.title('Project Manager Experience vs Salary')
plt.xlabel('Project Manager Experience')
plt.ylabel('Salary')
plt.scatter(dataset["Project Manager Experience"].head(n=50), dataset["Salary"].head(n=50), color="red") #color code is k or m or etc.,
#plt.axis([0, 25, 0, 25])
plt.grid(True)

plt.figure()
plt.title('Certifications vs Salary')
plt.xlabel('Certifications')
plt.ylabel('Salary')
plt.scatter(dataset["Certifications"].head(n=50), dataset["Salary"].head(n=50), color="purple") #color code is k or m or etc.,
#plt.axis([0, 25, 0, 25])
plt.grid(True)
plt.show()
