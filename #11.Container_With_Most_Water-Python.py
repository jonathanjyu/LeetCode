#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height)-1
        maxarea = 0
        while left < right:
            tmparea = (right-left)*min(height[left],height[right])
            if tmparea > maxarea:
                maxarea = tmparea
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxarea

