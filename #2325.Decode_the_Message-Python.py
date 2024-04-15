#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def decodeMessage(self, key, message):
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']
    exist = []
    ans = ""
    for i in range(len(key)):
        if key[i] not in exist and key[i] != ' ':
            exist.append(key[i])
    exist.append(' ')
    #print(exist)
    for i in range(len(message)):
        #print(exist.index(message[i]))
        ans = ans + str(alpha[exist.index(message[i])])
    return ans

