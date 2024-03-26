#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def isHappy(self, n):
    happyset = []
    while n not in happyset:
        happyset.append(n)
        n = str(n)
        tmp = 0
        for i in range(len(n)):
            tmp = tmp + int(n[i])**2
        n = tmp
        if n == 1:return True
        #elif n in happyset:return False
    return False

