#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def largestLocal(self, grid):
    ans = []
    for i in range(len(grid)-2):
        tmp2 = []
        for j in range(len(grid)-2):
            x = i + 1
            y = j + 1
            tmp = max(grid[x-1][y-1],grid[x][y-1],grid[x+1][y-1],grid[x-1][y],grid[x][y],grid[x+1][y],grid[x-1][y+1],grid[x][y+1],grid[x+1][y+1])
            tmp2.append(tmp)
        ans.append(tmp2)
    return ans

