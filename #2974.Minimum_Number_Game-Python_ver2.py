#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def numberGame(self, nums):
    ans = []
    nums = sorted(nums)
    for i in range(0,len(nums)-1,2):
        ans.append(nums[i+1])
        ans.append(nums[i])
    return ans

