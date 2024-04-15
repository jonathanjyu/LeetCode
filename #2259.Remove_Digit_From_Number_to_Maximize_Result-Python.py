#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def removeDigit(self, number, digit):
    maxnum = 0
    for i in range(len(number)):
        if number[i] == digit:
            #print(number[0:i]+number[i+1:])
            if int(number[0:i]+number[i+1:]) > maxnum:
                maxnum = int(number[0:i]+number[i+1:])
            #tmp = number[:]
    return str(maxnum)

