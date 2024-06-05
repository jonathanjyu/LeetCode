#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def productExceptSelf(self, nums):
    prefixpro = 1
    suffixpro = 1
    prefix = [1]
    suffix = [1]
    for i in range(len(nums)-1):
        prefixpro *= nums[i]
        prefix.append(prefixpro)
    for i in range(len(nums)-1,0,-1):
        suffixpro *= nums[i]
        suffix.append(suffixpro)
    suffix = suffix[::-1]
    for i in range(len(prefix)):
        prefix[i] = prefix[i] * suffix[i]

    return prefix

