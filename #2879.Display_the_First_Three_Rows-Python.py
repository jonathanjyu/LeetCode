#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)

