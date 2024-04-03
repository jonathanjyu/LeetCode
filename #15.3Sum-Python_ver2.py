#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def threeSum(self, nums):
    ans = []
    nums = sorted(nums)

    for i in range(len(nums)-2):
        j = i + 1
        k = len(nums) - 1
        while j < k:
            if (nums[i] + nums[j] + nums[k] == 0) and ([nums[i],nums[j],nums[k]] not in ans):
                ans.append([nums[i],nums[j],nums[k]])
                j += 1
                k -= 1
            elif nums[i] + nums[j] + nums[k] > 0:
                k -= 1
            else:
                j += 1
    return ans

