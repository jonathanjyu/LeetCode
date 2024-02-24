#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def isPalindrome(self, s):
    s = s.lower()
    s = ''.join([i for i in s if i.isalnum()])
    if s == s[::-1]:
        return True
    else:
        return False

