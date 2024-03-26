#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def containsNearbyDuplicate(self, nums, k):
    nums_set = {}
    for i in range(len(nums)):

        if nums[i] not in nums_set:
            nums_set[nums[i]] = i
        else:
            if i - nums_set[nums[i]] <= k:
                return True
            else:
                nums_set[nums[i]] = i
    return False

