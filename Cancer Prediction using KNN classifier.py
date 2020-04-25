#!/usr/bin/env python
# coding: utf-8

# # CANCER PREDICTION USING KNN ALGORITHM

# ### REQUIRED PACKAGES

# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split


# ### IMPORTING THE DATASET AS data

# In[8]:


data= pd.read_csv("data.csv")


# ### PREPROCESSING THE DATA

# In[ ]:


data = data.drop("id",axis=1) #to drop data in column wise axis=1 and for row wise axis=0


# In[15]:


data.shape #to see the dimension of the dataset


# In[17]:


data.describe() #to see the summary as the data


# In[20]:


data.isna().sum() #to see whether


# In[26]:


data.dtypes #to see the datatpye of each features


# ### TRAINING THE MODEL

# In[30]:


x=data.copy()
x=x.drop("diagnosis",axis=1)


# In[ ]:


data = data.drop("Unnamed: 32",axis=1)


# In[60]:


from sklearn.preprocessing import LabelEncoder #encoding the target variable
encoder=LabelEncoder()
data["diagnosis"]=encoder.fit_transform(data["diagnosis"])
data


# In[61]:


x=data.iloc[:,1:32] #assigning the training data or features to x


# In[64]:


y=data.iloc[:,0] #assigning the target to y


# In[76]:


x_train,x_test,y_train,y_test = train_test_split(x,y, test_size=0.2,random_state=47) #splitting the data into 4 parts


# In[73]:


knn=KNeighborsClassifier() #defining the model as knn


# In[77]:


knn.fit(x_train,y_train) #training our model


# ### PREDICTING THE TEST DATA USING THE MODEL

# In[79]:


knn.predict(x_test)


# ### ACCURACY OF OUR MODEL

# In[80]:


knn.score(x_test,y_test) #accuracy of the model

