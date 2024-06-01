#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def canCompleteCircuit(self, gas, cost):
    if sum(gas)-sum(cost) < 0:return -1
    diff = [gas[i]-cost[i] for i in range(len(gas))]
    #print(diff)

    tmpsum = 0
    start = 0
    for i in range(len(diff)):
        tmpsum += diff[i]
        if tmpsum < 0:
            tmpsum = 0
            start = i + 1
    return start

