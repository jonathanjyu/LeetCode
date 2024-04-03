#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def hIndex(self, citations):
    citations = sorted(citations)[::-1]
    #print(citations)
    count = 0
    for h in range(len(citations),0,-1):
        count = 0
        #print(h)
        for i in range(len(citations)):
            #print(i,citations[i])
            if citations[i] >= h:
                count += 1
                #print('count:',count)
        if count >= h:
            return h
    return 0

