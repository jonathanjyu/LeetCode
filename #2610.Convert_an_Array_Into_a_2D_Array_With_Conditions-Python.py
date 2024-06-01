#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def findMatrix(self, nums):
    numsmap = {}
    for i in nums:
        if i in numsmap:
            numsmap[i] += 1
        else:
            numsmap[i] = 1
    #print(numsmap)
    values = numsmap.values()
    keys = numsmap.keys()
    #print(keys,values)
    rowslen = max(values)
    ans = []
    for i in range(rowslen):
        tmp = []
        for j in range(len(keys)):
            if numsmap[keys[j]] > 0:
                tmp.append(keys[j])
                numsmap[keys[j]] -= 1
        ans.append(tmp)
    return ans

