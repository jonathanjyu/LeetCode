#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def removeElement(self, nums, val):
    count = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[count] = nums[i]
            count = count + 1
    return count

