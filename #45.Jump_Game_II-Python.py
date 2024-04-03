#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def jump(self, nums):
    jpcount = 0
    end = 0
    farest = 0

    for i in range(len(nums)-1):
        # find the farthest pos
        farest = max(farest, i+nums[i])
        if farest >= len(nums)-1:
            jpcount += 1
            break

        if i == end:
            jpcount += 1
            end = farest
    return jpcount

