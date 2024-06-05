#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def convert(self, s, numRows):
    if numRows == 1:return s
    ans = [[] for i in range(numRows)]
    #print(ans)

    direction = 1 # 0 for up 1 for down
    pos = 0 # run on s
    rowpos = 0 # run on rows
    while pos < len(s):
        ans[rowpos].append(s[pos])
        pos += 1
        if rowpos == 0:
            direction = 1
            rowpos = 1
        elif rowpos == numRows-1:
            direction = 0
            rowpos -= 1
        elif rowpos >= 0 and direction == 1:
            rowpos += 1
        elif rowpos >= 0 and direction == 0:
            rowpos -= 1
    #print(ans)
    for i in range(len(ans)):
        ans[i] = ''.join(ans[i])
    #print(''.join(ans))
    return ''.join(ans)

