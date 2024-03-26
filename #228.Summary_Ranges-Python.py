#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def summaryRanges(self, nums):
    nums_set = {}
    for i in range(len(nums)):
        # if nums[i]-1 in set, nums_set[] = nums[i]
        # nums_set[i] = j : from i -> j
        if nums[i]-1 in nums_set.values():
            nums_set[nums_set.keys()[nums_set.values().index(nums[i]-1)]] = nums[i]
        else:
            nums_set[nums[i]] = nums[i]
    #print(nums_set)
    ans = []
    for i in sorted(nums_set.keys()):
        if i == nums_set[i]:
            ans.append(str(i))
        else:
            ans.append(str(i)+"->"+str(nums_set[i]))
    return ans

