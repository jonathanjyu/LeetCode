#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def twoSum(self, nums, target
    for i in range(len(nums)):
        x = nums[i]
        y = target-x
        for j in range(i+1,len(nums)):
            if nums[j] == y:
                return [i,j]

