#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def appendCharacters(self, s, t):

    pointT = 0
    for i in range(len(s)):
        if s[i] == t[pointT]:
            pointT += 1

        if pointT >= len(t):
            return 0
    return len(t) - pointT

