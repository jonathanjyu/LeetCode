#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def __init__(self, n):
    self.ans = [None]*n
    self.ptr = 0
    """
    :type n: int
    """


def insert(self, idKey, value):
    idKey -= 1
    self.ans[idKey] = value
    if idKey > self.ptr:
        return []
    else:
        while self.ptr <= len(self.ans)-1 and self.ans[self.ptr] is not None:
            self.ptr += 1
        return self.ans[idKey:self.ptr]

