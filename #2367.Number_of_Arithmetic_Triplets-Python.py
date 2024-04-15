#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def arithmeticTriplets(self, nums, diff):
    x = range(len(nums))
    mapd = dict(zip(nums,x))
    count = 0
    for i in range(len(nums)-2):
        a = nums[i]+diff
        b = a+diff
        if a in mapd and b in mapd:
            count += 1
    return count

