#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def numSubarrayProductLessThanK(self, nums, k):
    count = 0
    left = 0
    product = 1
    for i in range(len(nums)):
        product = product * nums[i]
        while product >= k and left <= i:
            product = product / nums[left]
            left += 1
        if product < k:
            count = count + i - left + 1
    return count

