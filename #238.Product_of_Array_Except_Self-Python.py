#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def productExceptSelf(self, nums):
    prefix = [1]
    suffix = [1]
    ans = []
    pre = 1
    suf = 1
    for i in range(len(nums)-1):
        pre = pre * nums[i]
        prefix.append(pre)
    for i in range(len(nums)-1,0,-1):
        suf = suf*nums[i]
        suffix.append(suf)
    suffix = suffix[::-1]
    for i in range(len(nums)):
        ans.append(prefix[i]*suffix[i])
    return ans       

