#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def maxWidthOfVerticalArea(self, points):
    x = []
    ans = 0
    for i in range(len(points)):
        x.append(points[i][0])
    x = sorted(x)
    for i in range(len(x)-1):
        if abs(x[i+1]-x[i])>ans:
            ans = abs(x[i+1]-x[i])
    return ans

