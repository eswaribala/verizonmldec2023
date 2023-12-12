# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 09:29:52 2023

@author: Balasubramaniam
"""
import pandas as pd
from matplotlib import pyplot as plt
data=pd.read_csv("F:/verizonmldec2023/datasets/Position_Salaries.csv")
df=pd.DataFrame(data)
level=df['Level']
salary=df['Salary']

print(df["Level"],df["Salary"])
df = pd.DataFrame( {"Level":df["Level"], "Salary":df["Salary"]})
print(df)
x = df.values

from sklearn import preprocessing

min_max_scaler = preprocessing.MinMaxScaler()
x_scaled = min_max_scaler.fit_transform(x)
df = pd.DataFrame(x_scaled)
print(df)

# from sklearn.preprocessing import Normalizer
 
# scaler = Normalizer()
# scaled_data = scaler.fit_transform(df)
# scaled_df = pd.DataFrame(scaled_data,columns=df.columns)
# print(scaled_df)

fig=plt.figure(figsize=(10,5))
plt.scatter(df.iloc[:,0],df.iloc[:,1],color="red")
plt.title("Level vs Salary")
plt.xlabel("Level")
plt.ylabel("Salary")
#plt.xticks(range(0.0,0.8))
plt.legend(["Salary","Level"],loc="lower right")
plt.grid()
plt.show()


