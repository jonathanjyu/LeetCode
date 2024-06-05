#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def commonChars(self, words):
    alphe2 = list(set(words[0]))
    ans = []
    for i in alphe2:
        tmp = []
        for j in range(len(words)):
            tmp.append(words[j].count(i))
        if min(tmp) != 0:
            ans += [i]*min(tmp)
    return ans

