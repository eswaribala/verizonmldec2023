# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 14:38:40 2023

@author: Balasubramaniam
"""

import pandas as pd

df=pd.read_csv("F:/verizonmldec2023/datasets/churn-bigml-20.csv")
print("Data Frame", df)
print("Data Shape", df.shape)
print("Data length", len(df))
print("Data Columns", df.columns)
print("Data Index", df.index)
print("Total Day Calls", df['Total day calls'])
print("Total Day Calls", df.head)
print("Indexed Location", df.iloc[0:5, 1:3])

#find out the missing data
print("Count the missing values",df.isnull().sum())

usedcarsdf=pd.read_csv("F:/verizonmldec2023/datasets/used_cars_data.csv")
print("Count the missing values",usedcarsdf.isnull().sum())

print("% of missing values",(usedcarsdf.isnull().sum()/len(usedcarsdf))*100)


print("Average calls per day",df["Total day calls"].mean())
print("Average night calls per day",df["Total night calls"].mean())