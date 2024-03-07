#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students[students['student_id']==101][['name','age']]

