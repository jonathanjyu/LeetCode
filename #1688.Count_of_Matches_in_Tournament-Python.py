#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def numberOfMatches(self, n):
    matches = 0
    while n >= 2:
        if n % 2 == 1:
            tmp_match = ((n-1)/2)
            matches = matches + tmp_match
            n = tmp_match + 1
        else:
            tmp_match = n/2
            matches = matches + tmp_match
            n = tmp_match
    return matches

