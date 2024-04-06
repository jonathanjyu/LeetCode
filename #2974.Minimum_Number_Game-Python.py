#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def numberGame(self, nums):
    nums = sorted(nums,reverse = True)
    tmp = []
    ans = []
    while len(nums) > 0:
        tmp.append(min(nums))
        nums.pop()
        if len(tmp) == 2:
            ans.append(tmp[1])
            ans.append(tmp[0])
            tmp = []
    return ans

