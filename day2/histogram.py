# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 12:41:54 2023

@author: Balasubramaniam
"""

import pandas as pd
from matplotlib import pyplot as plt
df=pd.read_csv("F:/verizonmldec2023/datasets/train.csv")

print(df["ram"])

plt.hist(df['ram'],bins=25,color='red',edgecolor='blue')
plt.xlabel('RAM')
plt.ylabel("# of mobile phones")
plt.show()
