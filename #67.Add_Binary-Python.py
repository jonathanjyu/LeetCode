#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def addBinary(self, a, b):
    ans = ""
    i = len(a)-1
    j = len(b)-1
    carry = 0
    while (i >= 0) or (j >= 0) or (carry >= 1):
        print(a[i],b[j],carry)
        if i >= 0:
            carry = carry + int(a[i])
            i = i - 1

        if j >= 0:
            carry = carry + int(b[j])
            j = j - 1
        ans = ans + str(carry % 2)
        carry = int(carry // 2)

    return ans[::-1]

