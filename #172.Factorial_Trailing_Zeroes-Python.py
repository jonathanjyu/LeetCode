#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def trailingZeroes(self, n):
    # count the min number of 5 and 2
    map52 = {5:0,2:0}
    for i in range(1,n+1):
        print(i)
        while i % 2 == 0:
            map52[2] += 1
            i = i/2
        while i % 5 == 0:
            map52[5] += 1
            i = i/5
    return min(map52.values())

