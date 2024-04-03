#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def climbStairs(self, n):
    ans = []
    ans.append(1)
    ans.append(1)
    for i in range(2,n+1):
        ans.append(ans[i-1]+ans[i-2])
    return ans[-1]

