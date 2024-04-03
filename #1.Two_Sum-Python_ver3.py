#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def twoSum(self, nums, target):
    summap = {}
    for i in range(len(nums)):
        if (target - nums[i]) not in summap:
            summap[nums[i]] = i
        else:
            return [i,summap[target - nums[i]]]
    return []

