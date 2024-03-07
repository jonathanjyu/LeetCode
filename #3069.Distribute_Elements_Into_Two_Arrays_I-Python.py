#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def resultArray(self, nums):
    arr1 = [nums[0]]
    arr2 = [nums[1]]
    for i in range(2,len(nums)):
        if arr1[-1]>=arr2[-1]:
            arr1.append(nums[i])
        else:
            arr2.append(nums[i])

    ans = arr1 + arr2
    return ans

