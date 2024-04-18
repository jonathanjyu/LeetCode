#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def maximumNumberOfStringPairs(self, words):
    count = 0
    for i in range(len(words)):
        if words[i][::-1] in words and words[i] != words[i][::-1]:
            count += 1
    return count/2

