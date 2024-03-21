#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def canConstruct(self, ransomNote, magazine):
    mag_dict = {}
    for i in magazine:
        if i in mag_dict:
            mag_dict[i] = mag_dict[i] + 1
        else:
            mag_dict[i] = 1
    for j in ransomNote:
        if j in mag_dict:
            mag_dict[j] = mag_dict[j] - 1
            if mag_dict[j] < 0:return False
        else:
            return False
    return True

