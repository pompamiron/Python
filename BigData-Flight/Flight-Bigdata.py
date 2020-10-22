#!/usr/bin/env python
# coding: utf-8

# In[14]:


import pandas as pd
data1 = pd.read_csv('flights.csv',sep =',')
data1.info()


# In[15]:


import pandas as pd
data2 = pd.read_csv('airlines.csv',sep =',')
data2.info()


# In[7]:


data1.head()


# In[8]:


data2.head()


# In[9]:


data1.info()


# In[10]:


data2.info()


# In[11]:


print("columns:"+str(data1.shape[1]))


# In[12]:


print("rows:"+str(data1.shape[0]))


# In[13]:


print("columns:"+str(data2.shape[1]))


# In[14]:


print("rows:"+str(data2.shape[0]))


# In[15]:


data1[(data1.CANCELLED == 1)].shape


# In[16]:


data1.groupby('AIRLINE')['CANCELLED'].count()


# In[6]:


data3 = data1.groupby('AIRLINE')['CANCELLED'].count()


# In[17]:


data1[['DEPARTURE_DELAY','ARRIVAL_DELAY']].describe()


# In[4]:


nData = data1.dropna(subset=['DEPARTURE_DELAY','ARRIVAL_DELAY'])
nData.shape


# In[23]:


mdata = pd.merge(nData,data2, how='outer',
                 left_on='AIRLINE', right_on='IATA_CODE')
mdata = mdata.drop('IATA_CODE',1)
mdata.head() 


# In[25]:


averageDepartDelay = mdata.groupby('AIRLINE_x')['DEPARTURE_DELAY'].mean()


# In[26]:


averageDepartDelay.sort_values(ascending=False)


# In[27]:


averageDepartDelay.sort_values(ascending=True)


# In[28]:


month_flight = mdata.groupby('MONTH')['FLIGHT_NUMBER'].count()
mdata.groupby('MONTH')['FLIGHT_NUMBER'].count()


# In[29]:


march = mdata[mdata.MONTH == 3]


# In[31]:


march[['AIRLINE_x','FLIGHT_NUMBER','MONTH']].groupby(['AIRLINE_x','MONTH']).count().unstack().max()


# In[33]:


(mdata.groupby('ORIGIN_AIRPORT').size())


# In[34]:


neworigin = (mdata.groupby('ORIGIN_AIRPORT').size()).sort_values()
print(neworigin.tail(n=10))


# In[35]:


(mdata.groupby('DESTINATION_AIRPORT').size())


# In[36]:


neworigin = (mdata.groupby('DESTINATION_AIRPORT').size()).sort_values()
print(neworigin.tail(n=10))


# In[38]:


import numpy as np
mdata["Delays"] = np.where(mdata['DEPARTURE_DELAY' or 'ARRIVAL_DELAY'] > 0, 'D','NotD')
print(mdata)


# In[39]:


mdata.groupby('Delays').size()


# In[40]:


data1[['DEPARTURE_DELAY','ARRIVAL_DELAY']].dropna(how='any').shape


# In[41]:


averageDepartDelay = mdata.groupby('AIRLINE_x')['DEPARTURE_DELAY'].mean()


# In[47]:


averageDepartDelay.min()


# In[48]:


print(averageDepartDelay.idxmin())
print(averageDepartDelay.min())


# In[ ]:




