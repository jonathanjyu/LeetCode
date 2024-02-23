#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def majorityElement(self, nums):
    ans = {}
    for i in range(len(nums)):
        if nums[i] not in ans:
            ans[nums[i]] = 1
        else:
            ans[nums[i]] = ans[nums[i]]+1
    #return ans.keys()[ans.values().index(max(ans.values()))]
    for key,value in ans.items():
        if value > floor(len(nums)/2):
            return key

