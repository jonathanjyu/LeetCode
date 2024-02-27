#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def romanToInt(self, s):
    symbol = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    ans = 0
    lastV = symbol[s[-1]]
    for i in range(len(s)-1,-1,-1):
        nowV = symbol[s[i]]
        if nowV >= lastV:
            ans = ans + nowV
        else:
            ans = ans - nowV
        lastV = nowV
    return ans

