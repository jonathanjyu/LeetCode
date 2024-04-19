#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def sumOfMultiples(self, n):
    ans = 0
    for i in range(n+1):
        if (i % 3 == 0) or (i % 5 == 0) or (i % 7 == 0):
            ans += i
    return ans

