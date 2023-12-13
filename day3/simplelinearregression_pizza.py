# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pyplot as plt
import numpy as np
'''
Training Instance
'''
x = [[6],[7],[8],[9],[10],[11],[12],[13],[14],[16], [18]] #pizza diameter
print(x[0])
y = [[7], [9],[10], [13],[14], [15], [17],[18],[21], [22],[24]] #price in dollars
plt.figure()
plt.title('Pizza price plotted against diameter')
plt.xlabel('Diameter in inches')
plt.ylabel('Price in dollars')
plt.plot(x, y, 'b.') #color code is k or m or etc.,
plt.axis([0, 25, 0, 25])
plt.grid(True)
plt.show()


#Linear regression Algorithm to predict price

from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(x, y)
print ('A 13" pizza should cost: $%.2f' % model.predict([[17]]))



#Mean Sqaured Error
MSE=np.mean((17-model.predict([[11]]))**2)
print("Mean Sqaured Error %r" %(MSE))