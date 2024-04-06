#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def findWordsContaining(self, words, x):
    ans = []
    for i in range(len(words)):
        if x in words[i]:
            ans.append(i)
    return ans

