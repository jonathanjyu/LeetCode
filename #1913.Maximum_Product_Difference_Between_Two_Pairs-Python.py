#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def maxProductDifference(self, nums):
    nums.sort()
    return nums[-1]*nums[-2]-nums[0]*nums[1]

