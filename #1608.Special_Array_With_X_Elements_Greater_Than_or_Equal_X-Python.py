#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def specialArray(self, nums):
    numsmap = {}
    for i in nums:
        if i not in numsmap:
            numsmap[i] = 1
        else:
            numsmap[i] += 1
    #print(sorted(numsmap.keys()))
    keys = sorted(numsmap.keys())
    ans = 0
    for i in range(len(nums)+1):
        ans = 0
        for j in range(len(keys)):
            if keys[j] >= i:
                ans = ans + numsmap[keys[j]]
        #print(ans,i)
        if ans == i:
            return i
    return -1

