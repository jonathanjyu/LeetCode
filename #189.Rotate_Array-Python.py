#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def rotate(self, nums, k):
    if k > len(nums):
        k = k % len(nums)
    tmp = nums[-k:]
    for i in range(len(nums)-1,-1,-1):
        if i >= k:
            nums[i] = nums[i-k]
        else:
            nums[i] = tmp[i]
    return nums

