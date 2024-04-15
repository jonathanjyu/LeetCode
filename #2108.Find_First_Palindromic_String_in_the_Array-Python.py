#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def firstPalindrome(self, words):
    for i in words:
        if i == i[::-1]:return i
    return ""

