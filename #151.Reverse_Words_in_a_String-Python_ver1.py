#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def reverseWords(self, s):
    s = s.split(' ')
    ans = []
    for i in s:
        if i != '':
            ans.append(i)
    ans = ans[::-1]
    return ' '.join(ans)

