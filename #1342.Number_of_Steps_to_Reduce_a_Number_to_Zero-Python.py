#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def numberOfSteps(self, num):
    ans = 0
    while num >= 1:
        if num % 2 == 1:
            ans += 1
            num -= 1
        else:
            ans += 1
            num /= 2
    return ans

