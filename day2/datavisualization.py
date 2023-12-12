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



sns.boxplot(data = df.head(n=500), orient = "h")
plt.show()
pkmn_type_colors = ['#78C850',  # Grass
                    '#F08030',  # Fire
                    '#6890F0',  # Water
                    '#A8B820',  # Bug
                    '#A8A878',  # Normal
                    '#A040A0',  # Poison
                    '#F8D030',  # Electric
                    '#E0C068',  # Ground
                    '#EE99AC',  # Fairy
                    '#C03028',  # Fighting
                    '#F85888',  # Psychic
                    '#B8A038',  # Rock
                    '#705898',  # Ghost
                    '#98D8D8',  # Ice
                    '#7038F8',  # Dragon
                   ]
# Create plot
sns.violinplot(x='Year',
               y='Value', 
               data=df.head(n=15), 
               inner=None, # Remove the bars inside the violins
               palette=pkmn_type_colors)

