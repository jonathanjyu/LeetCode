#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    return customers.drop_duplicates(subset=['email'])

