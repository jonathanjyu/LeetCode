#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def reverseVowels(self, s):
    front = 0
    end = len(s)-1
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    if len(s) < 2:return s
    s = list(s)
    #print(s)
    while front <= end:
        while s[front] not in vowels:
            front += 1
            if front >= len(s)-1:break
        while s[end] not in vowels:
            end -= 1
            if end <= 0:break
        #print(front,s[front],end,s[end])
        if front > end:
            break
        tmp = s[end]
        s[end] = s[front]
        s[front] = tmp
        front += 1
        end -= 1
        #print(s)
    s = ''.join(s)
    return s

