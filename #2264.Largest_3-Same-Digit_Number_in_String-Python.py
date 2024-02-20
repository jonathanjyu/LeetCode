#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def largestGoodInteger(self, num):
    a = ["999","888","777","666","555","444","333","222","111","000"]
    for i in a:
        if i in num:
            return i
    return ""

