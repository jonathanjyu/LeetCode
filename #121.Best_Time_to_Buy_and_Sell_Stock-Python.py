#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def maxProfit(self, prices):
    left = 0
    right = 1
    maxprice = 0
    while right < len(prices):
        price = prices[right]-prices[left]
        if prices[left] <= prices[right]:
            if price > maxprice:
                maxprice = price
        else:
            left = right
        right = right + 1
    return maxprice

