#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def strStr(self, haystack, needle):
    needle_len = len(needle)
    for i in range(len(haystack)):
        if haystack[i] == needle[0]:
            if haystack[i:i+needle_len] == needle:
                return i
    return -1

