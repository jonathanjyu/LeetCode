#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def isAnagram(self, s, t):
    smap = {}
    tmap = {}
    for i in s:
        if i not in smap:
            smap[i] = 1
        else:
            smap[i] += 1
    for i in t:
        if i not in tmap:
            tmap[i] = 1
        else:
            tmap[i] += 1
    if len(smap.keys()) != len(tmap.keys()):return False
    for i in smap.keys():
        if i not in tmap.keys() or smap[i] != tmap[i]:
            return False
    return True

