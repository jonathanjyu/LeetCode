#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def countDistinct(self, nums, k, p):
    subarray = set()
    #tmp = ""
    for i in range(len(nums)):
        count = 0
        tmp = ""
        for j in range(i,len(nums)):
            print(nums[j])
            if nums[j] % p == 0:
                count += 1
            if count > k:
                break
            else:
                tmp = tmp + str(nums[j]) + ','
                subarray.add(tmp)
                #if tmp not in subarray:
                #    subarray.append(tmp)
                    #print(tmp)
    return len(subarray)

