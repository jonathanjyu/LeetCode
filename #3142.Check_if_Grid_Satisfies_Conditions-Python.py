#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def satisfiesConditions(self, grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if j < len(grid[0])-1:
                if grid[i][j] == grid[i][j+1]:
                    return False
            if i < len(grid)-1:
                if grid[i][j] != grid[i+1][j]:
                    return False
    return True

