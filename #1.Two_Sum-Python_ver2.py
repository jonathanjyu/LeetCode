#!/usr/bin/env python
# coding: utf-8

# In[ ]:


nums_set = {}
for i in range(len(nums)):
    if (target - nums[i]) in nums_set:
        return [i,nums_set[target - nums[i]]]
    nums_set[nums[i]] = i
return []

