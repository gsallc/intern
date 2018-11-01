
# coding: utf-8

# In[3]:


import lib.pandas_ex as code
import pandas as pd
import pytest
import unittest
import pandas.util.testing as put




class TestPandasModel(object):
    

    
    def test_read_data(self):
        
        model = code.describe_data()
        df = model.read_data()
        df2 = pd.read_csv('C:/Users/manaj/Documents/Python Scripts/frb-master/tests/DailyAverage_1.csv', index_col='Date')
        df3 = df.iloc[:500, :5]
        put.assert_frame_equal(df, df3)
        
        
    def test_avg(self):
    
        model = code.describe_data()
        df = model.read_data()
        df2 = pd.read_csv('C:/Users/manaj/Documents/Python Scripts/frb-master/tests/DailyAverage_1.csv', index_col='Date')
        df3 = df.iloc[:500, :5]
    
        means = df3.mean()
        mean_c = model.avg()
        put.assert_series_equal(means, mean_c)
        
    def test_mini(self):
    
        model = code.describe_data()
        df = model.read_data()
        df2 = pd.read_csv('C:/Users/manaj/Documents/Python Scripts/frb-master/tests/DailyAverage_1.csv', index_col='Date')
        df3 = df.iloc[:500, :5]
    
        mini = df3.min()
        mini_c = model.mini()
        put.assert_series_equal(mini, mini_c)
        
    def test_maxi(self):
    
        model = code.describe_data()
        df = model.read_data()
        df2 = pd.read_csv('C:/Users/manaj/Documents/Python Scripts/frb-master/tests/DailyAverage_1.csv', index_col='Date')
        df3 = df.iloc[:500, :5]
    
        maxi = df3.max()
        maxi_c = model.maxi()
        put.assert_series_equal(maxi, maxi_c)
        
     
    
    
    
    

