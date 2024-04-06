#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def maxDepth(self, s):
    maxdepth = 0
    depth = 0
    for i in range(len(s)):
        if s[i] == "(":
            depth += 1
            if depth > maxdepth: maxdepth = depth
        elif s[i] == ")":
            depth -= 1
    return maxdepth

