#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def sortPeople(self, names, heights):
    height_map = {}
    for i in range(len(heights)):
        height_map[heights[i]] = names[i]
    heights = sorted(heights,reverse = True)
    ans = []
    for i in heights:
        ans.append(height_map[i])
    return ans

