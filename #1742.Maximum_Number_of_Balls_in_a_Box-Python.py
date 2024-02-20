#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def countBalls(self, lowLimit, highLimit):
    ans={}
    for i in range(lowLimit,highLimit+1,1):
        tmp = 0
        while i // 10 != 0:
            tmp = tmp + i % 10
            i = i // 10
        tmp = tmp + i

        if tmp not in ans:
            ans[tmp]=1
        else:
            ans[tmp]= ans[tmp]+1
    return max(ans.values())

