#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def findIntersectionValues(self, nums1, nums2):
    num1 = set(nums1)
    num2 = set(nums2)
    ans = [0,0]
    for i in range(len(nums1)):
        if nums1[i] in num2:
            ans[0] += 1
    for i in range(len(nums2)):
        if nums2[i] in num1:
            ans[1] += 1
    return ans

