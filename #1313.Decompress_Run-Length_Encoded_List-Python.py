#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def decompressRLElist(self, nums):
    ans = []
    for i in range(0,len(nums)-1,2):
        ans.extend([nums[i+1]]*nums[i])
    return ans

