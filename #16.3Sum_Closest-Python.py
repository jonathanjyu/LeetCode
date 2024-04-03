#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def threeSumClosest(self, nums, target):
    nums = sorted(nums)
    minclosest = abs (nums[0] + nums[1] + nums[2] - target)
    ans = nums[0] + nums[1] + nums[2]
    for i in range(len(nums)-2):
        j = i+1
        k = len(nums)-1
        while j < k:
            tmp = nums[i] + nums[j] + nums[k]
            if abs(tmp-target) < minclosest:
                minclosest = abs(tmp-target)
                ans = tmp
            if tmp == target:
                j += 1
                k -= 1
            elif tmp > target:
                k -= 1
            else:
                j += 1
    return ans

