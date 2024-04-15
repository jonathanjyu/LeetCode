#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def maximumPrimeDifference(self, nums):
    primemap = {}
    for i in range(len(nums)):
        if nums[i] > 2:
            flag = False
            for j in range(2,nums[i],1):
                if (nums[i] % j) == 0:
                    flag = True
                    break
            if flag == False:
                primemap[i] = nums[i]
        elif nums[i] == 2:
            primemap[i] = nums[i]
    if len(primemap) == 1:return 0
    return max(primemap.keys())-min(primemap.keys())

