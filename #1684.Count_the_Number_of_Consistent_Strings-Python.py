#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def countConsistentStrings(self, allowed, words):
    allowed = list(set(allowed))
    flag = False
    ans = 0
    for i in range(len(words)):
        flag = False
        for j in range(len(words[i])):
            if words[i][j] not in allowed:
                flag = True
                break
        if flag == False:
            ans += 1
    return ans

