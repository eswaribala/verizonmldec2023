# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 16:27:53 2023

@author: Balasubramaniam
"""

import pandas as pd
import numpy as np

df=pd.read_csv("F:/verizonmldec2023/datasets/Data.csv")

X=df.iloc[:,1:3].values

print("Data set",df)

#handle missing data

from sklearn.impute import SimpleImputer

simpleImputer=SimpleImputer(missing_values=np.nan,strategy="mean")
print("X values", X)

simpleImputer = simpleImputer.fit(X[:,1:3])
X[:, 1:3] = simpleImputer.transform(X[:,1:3])
print(X)