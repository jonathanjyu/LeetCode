#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def minOperations(self, nums, k):
    nums = sorted(nums)
    count = 0
    for i in nums:
        if i < k:
            count += 1
    return count

