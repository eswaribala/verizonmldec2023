# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 23:39:26 2023

@author: Balasubramaniam
"""

# First, we'll import pandas, a data processing and CSV file I/O library
import pandas as pd
from sklearn.datasets import load_iris
# We'll also import seaborn, a Python graphing library
import warnings # current version of seaborn generates a bunch of warnings that we'll ignore
warnings.filterwarnings("ignore")
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="white", color_codes=True)

#load data
iris=load_iris()
column_name = iris.feature_names
# Next, we'll load the Iris flower dataset, which is in the "../input/" directory
irisdf = pd.DataFrame(iris.data)
irisdf.columns = column_name
# Let's see what's in the iris data - Jupyter notebooks print the result of the last thing you do
print(irisdf.head())
print(irisdf)
#scatter
irisdf.plot(kind="scatter", x="sepal length (cm)", y="sepal width (cm)")

# A seaborn jointplot shows bivariate scatterplots and univariate histograms in the same figure
sns.jointplot(x="sepal length (cm)", y="sepal width (cm)", data=irisdf, size=5)

sns.FacetGrid(irisdf,size=5) \
   .map(plt.scatter, "sepal length (cm)", "sepal width (cm)") \
   .add_legend()
   
