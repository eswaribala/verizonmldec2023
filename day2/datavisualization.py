# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 13:12:31 2023

@author: Balasubramaniam
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv("F:/verizonmldec2023/datasets/population.csv")
sns.set(style="white", color_codes=True)
#dual sim users
#scatter
# df.plot(kind="scatter", x="Year", y="Value")
# sns.FacetGrid(df,size=20) \
#    .map(plt.scatter, "Year", "Value") \
#    .add_legend()
   

sns.barplot(x = "Year", y = "Value",  data = df.head(n=25))
plt.show()


sns.swarmplot(x = "Year", y = "Value", data = df.head(n=25))
plt.show()



sns.stripplot(x = "Year", y = "Value", data = df.head(n=25))
plt.show()


