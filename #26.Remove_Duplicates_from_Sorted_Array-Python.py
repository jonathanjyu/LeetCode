#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def removeDuplicates(self, nums):
    exist = []
    count = 0
    for i in range(len(nums)):
        if nums[i] not in exist:
            exist.append(nums[i])
            nums[count] = nums[i]
            count = count + 1
    return count

