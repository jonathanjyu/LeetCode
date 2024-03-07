#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees['salary']*2
    return employees

