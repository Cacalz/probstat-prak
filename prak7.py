#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd

# Membaca file CSV
data_calista = pd.read_csv('C:/probstat/titanic.csv')

# Menampilkan beberapa baris pertama
print(data_calista)


# In[10]:


print(data_calista.columns)


# In[13]:


data1 = data_calista.loc[:,['Age','Pclass','ï»¿Survived']]
print(data1)


# In[14]:


data2 = data_calista[['Age', 'Pclass', 'ï»¿Survived']]
data2.plot(title='Persebaran Data', x='Age', y='Pclass', kind='scatter', c='ï»¿Survived', colormap='Paired')


# In[17]:


data3 = data_calista[['Name', 'Sex', 'Age', 'Pclass', 'Fare,,']]
penumpang = data3.groupby('Pclass')['Name'].nunique()
print('Jumlah Penumpang:\n', penumpang)


# In[18]:


data4 = data_calista[['Name', 'Sex', 'Age', 'Pclass', 'Fare,,', 'ï»¿Survived']]

# Menghitung jumlah penumpang yang tidak selamat berdasarkan Pclass
notsurvivedpassanger = data4.loc[data4['ï»¿Survived'] == 0]
print('Penumpang yang tidak survived:\n', notsurvivedpassanger['Pclass'].value_counts())

# Menghitung jumlah penumpang yang selamat berdasarkan Pclass
survivedpassanger = data4.loc[data4['ï»¿Survived'] == 1]
print('\nPenumpang yang survived:\n', survivedpassanger['Pclass'].value_counts())


# In[20]:


# Memilih kolom yang diperlukan
data_sex = data_calista[['Name', 'Sex']]

# Menghitung jumlah penumpang berdasarkan grup 'Sex'
jumlah_penumpang_sex = data_sex['Sex'].value_counts()

# Mencetak jumlah penumpang
print('Jumlah Penumpang berdasarkan Sex:\n', jumlah_penumpang_sex)


# In[22]:


# Memilih kolom yang diperlukan
data_survived_sex = data_calista[['Name', 'Sex', 'ï»¿Survived']]

# Memfilter data penumpang yang selamat berdasarkan jenis kelamin ('Sex')
survived_female = data_survived_sex.loc[(data_survived_sex['ï»¿Survived'] == 1) & (data_survived_sex['Sex'] == 'female')]
survived_male = data_survived_sex.loc[(data_survived_sex['ï»¿Survived'] == 1) & (data_survived_sex['Sex'] == 'male')]

# Mencetak jumlah penumpang yang selamat berdasarkan jenis kelamin
print('Jumlah Penumpang Selamat berdasarkan Sex:\nFemale:', len(survived_female), '\nMale:', len(survived_male))


# In[ ]:




