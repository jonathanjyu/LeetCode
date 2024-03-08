#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students['grade'] = students['grade'].astype(int)
    return students

