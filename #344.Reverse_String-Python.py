#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def reverseString(self, s):
    lens = 0
    if len(s) % 2 == 0:
        lens = len(s)//2
    else:
        lens = (len(s)//2) + 1
    #print(lens)
    for i in range(lens):
        tmp = s[i]
        s[i] = s[len(s)-i-1]
        s[len(s)-i-1] = tmp
    return s

