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

fig=plt.figure(figsize=(10,5))
plt.bar(level,salary,color="orange")
plt.title("Level vs Salary")
plt.xlabel("Level")
plt.ylabel("Salary")
plt.xticks(level)
plt.text(level,salary)
plt.legend(["Salary","Level"],loc="lower right")
plt.grid()
plt.show()