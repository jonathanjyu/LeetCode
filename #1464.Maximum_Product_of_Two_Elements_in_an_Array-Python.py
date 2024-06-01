#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def maxProduct(self, nums):
    largest = larger = 0
    if nums[1]>=nums[0]:
        largest = 1
        larger = 0
    else:
        largest = 0
        larger = 1
    for i in range(2, len(nums)):
        if nums[i] >= nums[largest]:
            larger = largest
            largest = i
        elif nums[i] < nums[largest] and nums[i] >= nums[larger]:
            larger = i
    return (nums[larger]-1)*(nums[largest]-1)

