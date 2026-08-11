#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


import numpy as np


# In[4]:


df=pd.read_csv("C:/Users/revat/Downloads/Telecom_Customer_Churn_Dataset.csv")


# In[5]:


df


# In[6]:


df.columns


# In[7]:


df.tail()


# In[8]:


df.head()


# In[9]:


df.describe()


# In[10]:


df.isnull().sum()


# # DATA PREPROCESSING

# In[11]:


from sklearn.preprocessing import LabelEncoder


# In[12]:


a=df.select_dtypes(include=('object'))


# In[13]:


a


# In[14]:


b= a.drop("CustomerID", axis =1 )


# In[15]:


b


# In[18]:


for i in b:
    b[i]=LabelEncoder().fit_transform(b[i])


# # feature scalling

# In[23]:


c=df.select_dtypes(include = np.number)


# In[26]:


c


# In[24]:


from sklearn.preprocessing import StandardScaler


# In[29]:


e=pd.DataFrame(StandardScaler().fit_transform(c),columns=['Tenure_Months','Monthly_Charges','Total_Charges'])


# In[40]:


df=pd.concat([b,e],axis=1)


# In[48]:


df


# # Feature Extraction

# In[49]:


y=df['Churn']  ##Target
x=df.drop("Churn",axis=1)    ##Feature


# # train_test_split

# In[50]:


from sklearn.model_selection import train_test_split


# In[51]:


x_test,x_train,y_test,y_train=train_test_split(x,y,test_size=0.2,random_state=42)


# # Model Deployment

# In[52]:


from sklearn.linear_model import LogisticRegression


# In[53]:


model = LogisticRegression()


# In[54]:


model


# In[55]:


model.fit(x_train,y_train)


# # predicting the churn

# In[59]:


data={'Contract_Type':[1],
      'Internet_Service':[1],
      'Payment_Method':[3],
      'Tenure_Months':[0.8],
      'Monthly_Charges':[0.7],w
      'Total_Charges':[0.8]}
new_customer=pd.DataFrame(data)


# In[60]:


new_customer


# In[61]:


print("model Prediction:",model.predict(new_customer))


# In[64]:


y_pred=model.predict(x_test)


# # Model Evalution

# In[65]:


from sklearn.metrics import accuracy_score,classification_report


# In[66]:


accuracy_score(y_test,y_pred)


# In[67]:


print(classification_report(y_test,y_pred))


# In[68]:


## to check why the customer has churn we use feature importance


# In[69]:


model.coef_[0]


# In[70]:


x.columns


# In[71]:


import matplotlib.pyplot as plt


# In[72]:


plt.barh(x.columns,model.coef_[0])


# In[ ]:




