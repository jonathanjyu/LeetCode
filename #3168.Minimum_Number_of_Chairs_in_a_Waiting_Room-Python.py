#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def minimumChairs(self, s):
    chair = 0
    maxchair = 0
    for i in range(len(s)):
        if s[i] == "E":
            chair += 1
        else:
            chair -= 1
        if chair > maxchair:
            maxchair = chair
    #print(maxchair)
    return maxchair

