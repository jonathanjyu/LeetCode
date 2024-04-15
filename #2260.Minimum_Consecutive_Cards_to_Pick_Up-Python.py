#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def minimumCardPickup(self, cards):
    min_len = len(cards)+1
    flag = False
    matchmap = {}
    for i in range(len(cards)):
        #print(i)
        if cards[i] not in matchmap:
            matchmap[cards[i]] = i
        else:
            tmp_len = i - matchmap[cards[i]] + 1
            if tmp_len < min_len:
                min_len = tmp_len
                flag = True
            #print(min_len,flag)
            matchmap[cards[i]] = i
    if flag == False:
        return -1
    else:
        return min_len

