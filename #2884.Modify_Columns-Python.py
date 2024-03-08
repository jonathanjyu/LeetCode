#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['salary'] = 2*employees['salary']
    return employees

