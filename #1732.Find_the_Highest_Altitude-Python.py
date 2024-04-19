#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def largestAltitude(self, gain):
    ans = 0
    alt = 0
    for i in range(len(gain)):
        alt = alt + gain[i]
        if alt > ans:
            ans = alt
    return ans

