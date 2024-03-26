#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def plusOne(self, digits):
    digits = digits[::-1]
    carry = 0
    for i in range(len(digits)):
        if i == 0:
            digits[i] = digits[i] + 1 + carry
        else:
            digits[i] = digits[i] + carry
        if digits[i] >= 10:
            digits[i] = digits[i] - 10
            carry = 1
        else:
            carry = 0
            break
    if carry == 1:
        digits.append(1)
    return digits[::-1]

