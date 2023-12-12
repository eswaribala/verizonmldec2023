# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 09:29:52 2023

@author: Balasubramaniam
"""
import pandas as pd
from matplotlib import pyplot as plt
data=pd.read_csv("F:/verizonmldec2023/datasets/population.csv")
df=pd.DataFrame(data)
level=df['Year']
salary=df['Value']

print(df["Year"],df["Value"])
df = pd.DataFrame( {"Level":df["Year"], "Salary":df["Value"]})
print(df)
x = df.values

from sklearn import preprocessing

min_max_scaler = preprocessing.MinMaxScaler()
x_scaled = min_max_scaler.fit_transform(x)
df = pd.DataFrame(x_scaled)
print(df)

# from sklearn.preprocessing import RobustScaler
 
# scaler = RobustScaler()
# scaled_data = scaler.fit_transform(df)
# scaled_df = pd.DataFrame(scaled_data,
#                          columns=df.columns)
# print(scaled_df.head())

fig=plt.figure(figsize=(10,5))
plt.scatter(df.iloc[:,0],df.iloc[:,1],color="red")
plt.title("Level vs Salary")
plt.xlabel("Level")
plt.ylabel("Salary")
#plt.xticks(plt.xticks(list(df.iloc[:,0])))
plt.legend(["Salary","Level"],loc="lower right")
plt.grid()
plt.show()


