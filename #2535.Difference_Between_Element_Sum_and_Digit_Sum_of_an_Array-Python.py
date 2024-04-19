#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def differenceOfSum(self, nums):
    esum = 0
    dsum = 0
    for i in range(len(nums)):
        esum += nums[i]
        while nums[i] >= 1:
            dsum += (nums[i]%10)
            nums[i] = nums[i] // 10
    return abs(esum-dsum)

