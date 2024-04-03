#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def threeSum(self, nums):
    ans = []
    for i in range(len(nums)-2):
        target = 0-nums[i]
        sumset = {}
        for j in range(i+1,len(nums)):
            if (target - nums[j]) not in sumset:
                sumset[nums[j]] = j
            else:
                tmp = sorted([nums[i],nums[j],target-nums[j]])
                if tmp not in ans:
                    ans.append(tmp)
    return ans

