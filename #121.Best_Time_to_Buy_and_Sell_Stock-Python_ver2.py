#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def maxProfit(self, prices):
    maxprofit = 0
    i = 0
    j = 1
    while j <= len(prices)-1:
        if prices[i] > prices[j]:
            i = j
        else:
            profit = prices[j]-prices[i]
            if profit > maxprofit:
                maxprofit = profit
        j += 1
    return maxprofit

