#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def isPalindrome(self, x):
    if x < 0 or (x > 0 and x % 10 == 0): return False
    t = int(x)
    y = 0
    while t >= 1:
        y = y*10 + t%10
        t = t // 10
        #print(y,t)
    return x==y

