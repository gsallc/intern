
# coding: utf-8

# In[40]:


import pandas as pd
import numpy as np
import unittest
from pandas.util.testing import assert_frame_equal


# In[49]:


class describe_data():
    
    def __init__(self):
        self.data = self.read_data()
            
    def read_data(self):
        df = pd.read_csv('C:/Users/manaj/Documents/Python Scripts/frb-master/lib/DailyAverage.csv', index_col='Date')
        df1 = df.iloc[:500, :5]
        return df1
    
    def avg(self):
        return self.data.mean()
    
    def std(self):
        return self.data.std()
    
    def mini(self):
        return self.data.min()
    
    def maxi(self):
        return self.data.max()

