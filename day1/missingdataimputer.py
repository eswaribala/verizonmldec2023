# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 16:27:53 2023

@author: Balasubramaniam
"""

import pandas as pd
import numpy as np

df=pd.read_csv("F:/verizonmldec2023/datasets/Data.csv")

X = df.iloc[:, :-1].values

print("Data set",df)

#handle missing data

# Taking care of missing data
from sklearn.impute import SimpleImputer

imputer = SimpleImputer(missing_values = np.nan, strategy = 'mean',verbose=0)

imputer = imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])
print(X)