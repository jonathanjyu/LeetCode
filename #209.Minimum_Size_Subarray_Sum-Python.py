#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    def minSubArrayLen(self, target, nums):
        if target in nums:return 1
        i = 0
        j = 0
        tmpsum = 0
        minlen = len(nums)+1
        while j < len(nums):
            tmpsum += nums[j]
            while tmpsum >= target:
                tmpsum -= nums[i]
                minlen = min(j-i+1,minlen)
                i += 1
            j += 1
        
        if minlen > len(nums):
            return 0
        else:
            return minlen

