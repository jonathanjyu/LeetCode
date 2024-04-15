#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def findLatestTime(self, s):
    ans = ""
    for i in range(len(s)):
        if s[i] == "?" and i == 0:
            if s[i+1] != "?" and int(s[i+1]) >= 2:
                ans = ans + "0"
            else:
                ans = ans + "1"
        elif s[i] == "?" and i == 1:
            if s[i-1] == "0":
                ans = ans + "9"
            else :
                ans = ans + "1"
        elif i == 2:
            ans = ans + ":"
        elif s[i] == "?" and i == 3:
            ans = ans + "5"
        elif s[i] == "?" and i == 4:
            ans = ans + "9"
        else:
            ans = ans + s[i]
    return ans

