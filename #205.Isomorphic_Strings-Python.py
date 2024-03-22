#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def isIsomorphic(self, s, t):
    if len(set(s)) == len(set(t)) == len(set(zip(s,t))):
        return True
    else:
        return False

