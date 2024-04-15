#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def checkIfPangram(self, sentence):
    ans = ""
    for i in sentence:
        if i not in ans:
            ans = ans + i
    if len(ans) == 26:return True
    else:return False

