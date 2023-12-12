# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 07:57:27 2023

@author: Balasubramaniam
"""

import numpy as np  
from scipy import stats  

# Population Mean 
mu = 10

# Sample Size
N1 = 21

# Degrees of freedom  
dof = N1 - 1

# Generate a random sample with mean = 11 and standard deviation = 1
x = np.random.randn(N1) + 11

# Using the Stats library, compute t-statistic and p-value
t_stat, p_val = stats.ttest_1samp(a=x, popmean = mu)
print("t-statistic = " + str(t_stat))  
print("p-value = " + str(p_val)) 