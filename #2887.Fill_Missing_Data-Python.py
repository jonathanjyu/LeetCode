#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    products = products.fillna(value = {'quantity':0})
    return products

