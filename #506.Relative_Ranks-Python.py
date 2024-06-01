#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def findRelativeRanks(self, score):
    scoremap = {}
    for i in range(len(score)):
        scoremap[score[i]] = i
    #print(scoremap)

    score = sorted(score)[::-1]

    ans = ["" for _ in range(len(score))]
    #print(ans)
    for i in range(len(score)):
        if i == 0:
            ans[scoremap[score[i]]]="Gold Medal"
        elif i == 1:
            ans[scoremap[score[i]]]=("Silver Medal")
        elif i == 2:
            ans[scoremap[score[i]]]=("Bronze Medal")
        else:
            ans[scoremap[score[i]]]=(str(i+1))
    #print(ans)
    return ans

