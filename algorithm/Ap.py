
# coding: utf-8

# In[144]:

array_length = 100


# In[145]:

from sklearn.cluster import AffinityPropagation
from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs


# In[146]:

import  numpy as np


# In[147]:

array = np.ndarray(shape=(20,array_length), dtype=float, order='F')


# In[148]:

import math
import random


# In[149]:

for j in range(0, 5):
    for i in range(0, array_length):
        array[j][i] = math.sin(i/10.0)*i+random.random()


# In[150]:

for j in range(5, 10):
    for i in range(0, array_length):
        array[j][i] = math.cos(i/10.0)*i+random.random()


# In[151]:

for j in range(10, 15):
    for i in range(0, array_length):
        array[j][i] = math.sin(i/10.0)*i+random.random()


# In[152]:

for j in range(15, 20):
    for i in range(0, array_length):
        array[j][i] = i*math.cos(i/10.0)*i+random.random()


# In[153]:

af = AffinityPropagation(preference=-50).fit(array)


# In[154]:

import numpy as np
import matplotlib.pyplot as plt

plt.close('all')
plt.figure(1)
plt.clf()
x = np.arange(0, array_length, 1);
for i in range(0 , 20):
    y = array[i]
    plt.plot(x, y, '#eeefff')

for i in af.cluster_centers_indices_:
    y = array[i]
    plt.plot(x, y, 'r')
plt.show()


# In[67]:




# In[ ]:



