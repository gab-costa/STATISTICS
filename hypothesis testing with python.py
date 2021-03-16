#!/usr/bin/env python
# coding: utf-8

# # Hypothesis Testing
# 
# From lecture, we know that hypothesis testing is a critical tool in determing what the value of a parameter could be.
# 
# We know that the basis of our testing has two attributes:
# 
# **Null Hypothesis: $H_0$**
# 
# **Alternative Hypothesis: $H_a$**
# 
# The tests we have discussed in lecture are:
# 
# * One Population Proportion
# * Difference in Population Proportions
# * One Population Mean
# * Difference in Population Means
# 
# In this tutorial, I will introduce some functions that are extremely useful when calculating a t-statistic and p-value for a hypothesis test.
# 
# Let's quickly review the following ways to calculate a test statistic for the tests listed above.
# 
# The equation is:
# 
# $$\frac{Best\ Estimate - Hypothesized\ Estimate}{Standard\ Error\ of\ Estimate}$$ 
# 
# We will use the examples from our lectures and use python functions to streamline our tests.

# In[2]:


import numpy as np
import statsmodels.api as sm
import pandas as pd


# ### One Population Proportion
# 
# #### Research Question 
# 
# In previous years 52% of parents believed that electronics and social media was the cause of their teenager’s lack of sleep. Do more parents today believe that their teenager’s lack of sleep is caused due to electronics and social media? 
# 
# **Population**: Parents with a teenager (age 13-18)  
# **Parameter of Interest**: p  
# **Null Hypothesis:** p = 0.52  
# **Alternative Hypthosis:** p > 0.52 (note that this is a one-sided test)
# 
# 1018 Parents
# 
# 56% believe that their teenager’s lack of sleep is caused due to electronics and social media.

# In[3]:


n=1018
pnull=.52
phat=.56
z1, p1 = sm.stats.proportions_ztest(phat*n, n , pnull) # the answer, first is the z test, second the p-value
print(f'the z test is {z1} and the p-value is {p1}')
# how p-value is lower than alpha, .95, we reject null hypothesis


# ### Difference in Population Proportions
# 
# #### Research Question
# 
# Is there a significant difference between the population proportions of parents of black children and parents of Hispanic children who report that their child has had some swimming lessons?
# 
# **Populations**: All parents of black children age 6-18 and all parents of Hispanic children age 6-18  
# **Parameter of Interest**: p1 - p2, where p1 = black and p2 = hispanic  
# **Null Hypothesis:** p1 - p2 = 0  
# **Alternative Hypthosis:** p1 - p2 $\neq$ = 0  
# 
# 
# 91 out of 247 (36.8%) sampled parents of black children report that their child has had some swimming lessons.
# 
# 120 out of 308 (38.9%) sampled parents of Hispanic children report that their child has had some swimming lessons.

# In[4]:


n1=247
p1=.37

n2=308
p2=.39

population1 = np.random.binomial(1,p1, n1)
population2 = np.random.binomial(1,p2,n2)

sm.stats.ttest_ind(population1, population2) #calculating t_test

#how p-value is greater than 0.05, we can not reject the null hypothesis







# ### One Population Mean
# 
# #### Research Question 
# 
# Is the average cartwheel distance (in inches) for adults 
# more than 80 inches?
# 
# **Population**: All adults  
# **Parameter of Interest**: $\mu$, population mean cartwheel distance.
# **Null Hypothesis:** $\mu$ = 80
# **Alternative Hypthosis:** $\mu$ > 80
# 
# 25 Adults
# 
# $\mu = 82.46$
# 
# $\sigma = 15.06$

# In[ ]:




