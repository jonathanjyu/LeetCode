#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def sampleStats(self, count):
    ans = []

    # minimum
    for i in range(len(count)):
        if count[i]!=0:
            minimum = float(i)
            break

    ans.append(minimum)

    # maximum
    for i in range(len(count)-1,-1,-1):
        if count[i]!=0:
            maximum = float(i)
            break

    ans.append(maximum)

    # mean
    summary = 0
    total_number = 0
    for i in range(len(count)):
        if count[i]!=0:
            total_number = total_number+count[i]
            summary = summary + i*count[i]
    mean = float(summary)/float(total_number)

    ans.append(mean)

    #median
    median = 0
    tmp = 0
    if total_number % 2 == 0:
        j = total_number/2
        k = j+1
        for i in range(len(count)):
            tmp = tmp + count[i]
            if tmp >= j:
                median = median+i
                break
        tmp = 0
        for i in range(len(count)):
            tmp = tmp + count[i]
            if tmp >= k:
                median = median+i
                break
        median = float(median)/2.
    else:
        j = int(total_number/2)+1
        for i in range(len(count)):
            tmp = tmp + count[i]
            if tmp >= j:
                median = float(i)
                break

    ans.append(median)

    # mode
    mode = float(count.index(max(count)))
    ans.append(mode)

    return ans

