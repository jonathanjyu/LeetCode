#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def __init__(self):
    self.data_map = {}
    self.data = []
    self.data_len = 0

def insert(self, val):
    if val in self.data:
        return False
    else:
        self.data.append(val)
        self.data_map[val] = self.data_len
        self.data_len += 1
        return True
    """
    :type val: int
    :rtype: bool
    """
def remove(self, val):

    if val not in self.data:
        return False
    else:
        tmp = self.data[-1]
        tmpi = self.data_map[val]

        self.data[-1] = val
        self.data[tmpi] = tmp
        self.data_map[tmp] = tmpi
        self.data.pop()
        self.data_map.pop(val)
        self.data_len -= 1
        return True
    """
    :type val: int
    :rtype: bool
    """


def getRandom(self):
    return random.choice(self.data)
    """
    :rtype: int
    """

