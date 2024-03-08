#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    return students.dropna(subset = 'name')
    

