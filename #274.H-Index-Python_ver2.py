#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def hIndex(self, citations):
    citations = sorted(citations)[::-1]
    count = 0
    for i in range(len(citations)):
        if citations[i] >= i+1:
            count = i+1
    return count

