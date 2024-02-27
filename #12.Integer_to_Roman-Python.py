#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def intToRoman(self, num):
    symbol = {1:"I",4:"IV",5:"V",9:"IX",10:"X",40:"XL",50:"L",90:"XC",100:"C",400:"CD",500:"D",900:"CM",1000:"M"}
    ans = ""
    keys = sorted(symbol.keys(),reverse = True)
    for i in keys:
        while num >= i:
            ans = ans + symbol[i]
            num = num - i

    return ans

