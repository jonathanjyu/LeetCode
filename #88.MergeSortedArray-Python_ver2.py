#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def merge(self, nums1, m, nums2, n):
    leg= m + n
    pos = leg-1
    m = m-1
    n = n-1
    while m>=0 and n>=0:
        if nums1[m]>=nums2[n]:
            nums1[pos] = nums1[m]
            m = m-1
        else:
            nums1[pos] = nums2[n]
            n = n-1
        pos = pos-1

    while m>=0:
        nums1[pos] = nums1[m]
        pos = pos-1
        m = m-1
    while n>=0:
        nums1[pos] = nums2[n]
        pos = pos-1
        n = n-1
    return nums1

