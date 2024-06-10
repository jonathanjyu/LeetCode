#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    def valueAfterKSeconds(self, n, k):
        i = 1 # run on time k 0 to k
        ans = [1]*n
        while i <= k:
            for j in range(1,n):
                ans[j] = ans[j-1]+ans[j]
            
            i += 1
        return ans[n-1] % (10**9 + 7)

