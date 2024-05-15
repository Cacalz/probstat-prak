#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score, KFold, GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier  # Added this line
from sklearn.metrics import confusion_matrix, accuracy_score


# In[4]:


data_calista = pd.read_csv('C:\probstat\houseprice.csv') 
data_calista.head(5)


# In[5]:


col_list = ['Price']
numhouse = data_calista[data_calista.columns[data_calista.columns.isin(col_list)]]

plt.figure(figsize=(10, 5))
numhouse.boxplot(sym='r*', grid=False)
plt.show()


# In[7]:


plt.figure(figsize=(15, 5))

plt.subplot(121)
data_calista['Price'].plot.hist(bins=10, title='Price')

plt.show()


# In[8]:


col_list=['Price', 'SqFt']
numhouse = data_calista[data_calista.columns[data_calista.columns.isin(col_list)]]
numhouse.plot.scatter(x='SqFt', y='Price')


# In[10]:


col_list = ['Price', 'Bedrooms']
numhouse = data_calista[col_list]
plt.figure(figsize=(15, 5))
numhouse.boxplot(by='Bedrooms')
plt.show()


# In[11]:


plt.figure(figsize=(10, 6))
plt.scatter(data_calista['Bedrooms'], data_calista['Price'], alpha=0.5)
plt.title('Scatter Plot Harga Rumah Berdasarkan Bedrooms')
plt.xlabel('Bedrooms')
plt.ylabel('Price')
plt.grid(True)
plt.show()


# In[12]:


plt.figure(figsize=(10, 6))
data_calista.boxplot(column='Price', by='Bathrooms')
plt.title('Grouped Boxplot Berdasarkan Bathrooms')
plt.xlabel('Bathrooms')
plt.ylabel('Price')
plt.grid(True)
plt.show()


# In[13]:


plt.figure(figsize=(10, 6))
plt.scatter(data_calista['Bathrooms'], data_calista['Price'], alpha=0.5)
plt.title('Scatter Plot Harga Rumah Berdasarkan Bathrooms')
plt.xlabel('Bathrooms')
plt.ylabel('Price')
plt.grid(True)
plt.show()


# In[ ]:




