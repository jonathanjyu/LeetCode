#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return [len(players),len(players.iloc[0])]

    #return list(players.shape)
    
    #pdsize = [players.shape[0],players.shape[1]]
    #return pdsize

