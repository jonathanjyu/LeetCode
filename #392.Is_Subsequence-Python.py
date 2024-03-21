#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def isSubsequence(self, s, t):
    s = list(s)
    if len(s) == 0:return True
    t = list(t)
    pt = 0
    ps = 0
    while pt < len(t):
        if t[pt] == s[ps]:
            ps = ps + 1
        pt = pt + 1
        if ps == len(s):return True
    return False

