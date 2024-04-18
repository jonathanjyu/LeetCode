#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def destCity(self, paths):
    path_map = {}
    for i in range(len(paths)):
        path_map[paths[i][0]] = paths[i][1]

    for i in range(len(path_map.values())):
        if path_map.values()[i] not in path_map.keys():
            return path_map.values()[i]

