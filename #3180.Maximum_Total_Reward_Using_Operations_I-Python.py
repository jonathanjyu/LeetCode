#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    def maxTotalReward(self, rewardValues):
        rewardValues.sort()
        pos = set()

        for i in rewardValues:
            dp = pos.copy()
            #print('before dp:',dp)
            #print('before pos:',pos)
            for j in pos:
                if j < i:
                    dp.add(i+j)
            dp.add(i)
            pos = dp
            #print('after dp:',dp)
            #print('after pos:',pos)
        return max(dp)

