#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    def twoSum(self, numbers, target):
        tmp = {}
        for i in range(len(numbers)):
            if target-numbers[i] not in tmp:
                tmp[numbers[i]] = i
            else:
                return[tmp[target-numbers[i]]+1,i+1]

