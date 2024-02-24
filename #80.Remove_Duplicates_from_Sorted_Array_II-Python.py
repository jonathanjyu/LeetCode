#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def removeDuplicates(self, nums):
    last_num = nums[0]
    ans_count = 1
    count = 1
    pos = 1
    for i in range(1,len(nums)):
        if nums[i]==last_num:
            if count == 2:
                count = 2
            else:
                ans_count = ans_count + 1
                count = count + 1
                nums[pos] = nums[i]
                pos = pos + 1 
        else:
            ans_count = ans_count + 1
            count = 1
            last_num = nums[i]
            nums[pos] = nums[i]
            pos = pos + 1
    return ans_count

