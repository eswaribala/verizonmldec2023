# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 12:19:43 2023

@author: Balasubramaniam
"""

import pandas as pd
from matplotlib import pyplot as plt
df=pd.read_csv("F:/verizonmldec2023/datasets/Position_Salaries.csv")
#pd.set_option('display.max_rows', df.shape[0]+1)
#pd.set_option('display.max_columns', 500)
#pd.set_option('display.width', 1000)

print(df["Level"],df["Salary"])
df = pd.DataFrame( {"Level":df["Level"], "Salary":df["Salary"]})
print(df)
x = df.values

import numpy as np

stdev=np.std(df.iloc[:,1])
variance=np.var(df.iloc[:,1])

print("The Salary closer to mean value", stdev)
print("The Salary Variance", variance)