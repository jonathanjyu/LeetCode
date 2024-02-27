#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def canJump(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    tmp = 0
    for i in range(len(nums)):
        if tmp < 0: return False
        else:
            if nums[i] > tmp:
                tmp = nums[i]
        tmp = tmp - 1
    return True

