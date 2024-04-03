#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def fourSum(self, nums, target):
        nums = sorted(nums)
        ans = []
        for i in range(len(nums)-3):
            for j in range(i+1,len(nums)-2):
                k = j + 1
                l = len(nums)-1
                while k < l:
                    if (nums[i]+nums[j]+nums[k]+nums[l]==target):
                        if ([nums[i],nums[j],nums[k],nums[l]] not in ans):
                            ans.append([nums[i],nums[j],nums[k],nums[l]])
                        k += 1
                        l -= 1
                    elif (nums[i]+nums[j]+nums[k]+nums[l]>target):
                        l -= 1
                    else:
                        k += 1
        return ans

