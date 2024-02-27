#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def lengthOfLastWord(self, s):
    s = s.split()
    return len(s[-1])

