# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 15:47:20 2018

@author: Balasubramaniam
"""

# Polynomial Regression

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_excel('AngolaPolynomial.xlsx')
X = dataset.iloc[:, 0:1].values
y = dataset.iloc[:, 1].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)

# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)"""

# Fitting Linear Regression to the dataset
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X_train, y_train)

# Fitting Polynomial Regression to the dataset
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree =4)
X_poly = poly_reg.fit_transform(X_train)
print(X_poly)
#poly_reg.fit(X_poly, y)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly, y_train)

import statsmodels.api as sm

est = sm.OLS(y_train, X_poly) #ordinary least square method 
est2 = est.fit()
print("Summary.....")
print(est2.summary())


# Visualising the Linear Regression results
plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_test, lin_reg.predict(X_test), color = 'blue')
plt.title('Truth or Bluff (Linear Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()


# Visualising the Polynomial Regression results
plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_test, lin_reg_2.predict(poly_reg.fit_transform(X_test)), color = 'blue')
plt.title('Truth or Bluff (Polynomial Regression)')
plt.xlabel('Year')
plt.ylabel('Population')
plt.show()

# Visualising the Polynomial Regression results (for higher resolution and smoother curve)
X_grid = np.arange(min(X_train), max(X_train), 0.1)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_grid, lin_reg_2.predict(poly_reg.fit_transform(X_grid)), color = 'blue')
plt.title('Truth or Bluff (Polynomial Regression)')
plt.xlabel('Year')
plt.ylabel('Population')
plt.show()
