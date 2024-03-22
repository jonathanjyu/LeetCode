#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def wordPattern(self, pattern, s):
    if len(set(pattern)) == len(set(s.split(' '))) == len(set(zip(pattern, s.split(' ')))) and len(pattern) == len(s.split(' ')):
        return True
    else:return False

