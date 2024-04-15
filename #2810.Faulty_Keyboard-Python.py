#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def finalString(self, s):
    ans = ""
    for i in range(len(s)):
        if s[i] != 'i':
            ans = ans + s[i]
        else:
            ans = ans[::-1]
    return ans

