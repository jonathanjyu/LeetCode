#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    def numberOfChild(self, n, k):
        i = 0 # run on time k: 0 to k
        dire = 1 # 1 for right; 0 for left
        j = 0 #run on children n: 0 to n-1
        while i < k:
            if j == 0:
                j = 1
                i += 1
                dire = 1
            elif j == n-1:
                j = n-2
                i += 1
                dire = 0
            elif dire == 1:
                j += 1
                i += 1
            elif dire == 0:
                j -= 1
                i += 1
        return j
                

