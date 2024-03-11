#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    return weather.pivot(index = 'month', columns = 'city', values = 'temperature')

