#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def reverseWords(self, s):
    s = s.split()
    s = s[::-1]
    return ' '.join(s)

