#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def scoreOfString(self, s):
    sums = 0
    for i in range(len(s)-1):
        sums = sums + abs(int(ord(s[i]))-int(ord(s[i+1])))
    return sums

