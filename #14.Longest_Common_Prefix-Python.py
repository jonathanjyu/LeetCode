#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def longestCommonPrefix(self, strs):
    min_len = len(strs[0])
    min_len_str = strs[0]
    for i in range(1,len(strs)):
        if len(strs[i]) < min_len:
            min_len = len(strs[i])
            min_len_str = strs[i]
    ans = min_len_str
    for i in range(min_len,0,-1):
        for j in range(len(strs)):
            if strs[j][0:i] != ans:
                ans = ans[0:-1]
                break
            else:
                if j == len(strs)-1:
                    return ans
    return ""

