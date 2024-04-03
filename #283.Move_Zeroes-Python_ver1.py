#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def moveZeroes(self, nums):
    pos_nonzero = 0
    if len(nums) <= 1: return nums
    for i in range(len(nums)):
        if nums[i] == 0:
            pos_nonzero = i
            while nums[pos_nonzero] == 0 and pos_nonzero < len(nums)-1:
                #print(nums[pos_nonzero])
                pos_nonzero += 1
            #print(nums[i],pos_nonzero)
            tmp = nums[pos_nonzero]
            nums[pos_nonzero] = 0
            nums[i] = tmp
            #print(nums)
    return nums

