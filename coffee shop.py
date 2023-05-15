#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv ("Bangalore_cafe_dataset.csv")
df


# In[14]:


df.tail()


# In[2]:


df.info()


# In[3]:


#STATISTICAL INFORMATION
df.describe() 


# In[9]:


#FIRST FIVE
df.head()


# In[41]:


colors  = ("darkorange", "green")
explodes = [0.5, 0.5]

df["online_order"].value_counts(sort=False).plot.pie(colors=colors,
                                                 textprops={'fontsize': 12}, 
                                                 autopct = '%4.1f',
                                                 startangle= 90, 
                                                 radius =2, 
                                                 rotatelabels=True,
                                                 shadow = True)


# In[43]:


print("No. of cafe with table booking facility:")
(df.book_table == 'Yes').sum()


# In[47]:


print("All unique cafe ratings:")
df.rate.unique()


# In[10]:


#COLUMN NAMES
df.columns


# In[11]:


#DIMENSION
df.ndim


# In[12]:


#correlation between columns
df.corr()


# In[13]:


df.corr(method = 'spearman')


# In[19]:


df.corr(method = 'kendall')


# In[23]:


import seaborn as sns
data_heatmap = df.corr(method = 'kendall')
sns.heatmap(data_heatmap)
import matplotlib.pyplot as plt
plt.figure(facecolor='yellow')


# In[25]:


df.isnull().sum()


# In[27]:


#Analysis of cafe based on their Online Delivery
print("No. of cafe with online delivery:")
(df.online_order == 'Yes').sum()


# In[55]:


# MOST LIKED DISHES IN BANGALORE
import re
df=df[df['dish_liked'].notnull()]
df.index=range(df.shape[0])
likes=[]
for i in range(df.shape[0]):
    splited_array=re.split(',',df['dish_liked'][i])
    for item in splited_array:
        likes.append(item)

print("Count of Most liked dishes of Bangalore")
favourite_food = pd.Series(likes).value_counts()
favourite_food.head(5)


# In[8]:


sns.countplot(x=df['online_order'])
fig = plt.gcf()
fig.set_size_inches(6,6)
plt.title('cafe delivering online or not')

