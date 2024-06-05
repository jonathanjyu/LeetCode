#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def longestPalindrome(self, s):
    letter_map = {}
    for i in range(len(s)):
        if s[i] not in letter_map:
            letter_map[s[i]] = 1
        else:
            letter_map[s[i]] += 1

    values = letter_map.values()
    ans = 0
    oddnum = 0

    for i in range(len(values)):
        if values[i] % 2 == 1:
            oddnum += 1
        ans += values[i]

    if oddnum > 1:
        ans -= (oddnum - 1)
    return ans

