#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def countKDifference(self, nums, k):
    num_map = {}
    for i in range(len(nums)):
        if nums[i] not in num_map:
            num_map[nums[i]] = 1
        else:
            num_map[nums[i]] += 1
    #print(num_map)
    count = 0
    for i in range(len(nums)):
        if (k + nums[i]) in num_map:
            count = count + num_map[k+nums[i]]

        if (-k + nums[i]) in num_map:
            count = count + num_map[-k+nums[i]]
    count = count / 2
    return count

