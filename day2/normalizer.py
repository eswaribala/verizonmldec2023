# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 10:41:37 2023

@author: Balasubramaniam
"""
import pandas as pd
from matplotlib import pyplot as plt
df=pd.read_csv("F:/verizonmldec2023/datasets/population.csv")
pd.set_option('display.max_rows', df.shape[0]+1)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

print(df["Year"],df["Value"])
df = pd.DataFrame( {"Year":df["Year"], "Population":df["Value"]})
print(df)
x = df.values

from sklearn import preprocessing

min_max_scaler = preprocessing.MinMaxScaler()
min_max_scaler = preprocessing.MinMaxScaler()
x_scaled = min_max_scaler.fit_transform(x)
df = pd.DataFrame(x_scaled)
print(df)