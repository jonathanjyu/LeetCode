#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def maxSubArray(self, nums):
    if len(nums) < 2:return nums[0]
    maxsum = nums[0]+nums[1]
    tmpsum = 0
    start = 0
    end = 0
    s = 0
    for i in range(len(nums)):
        tmpsum = tmpsum + nums[i]
        if tmpsum > maxsum:
            maxsum = tmpsum
            start = s
            end = i
        if tmpsum < 0:
            tmpsum = 0
            s = i + 1
    #print(nums[start:end+1]) ## print maximum subarray
    return maxsum

