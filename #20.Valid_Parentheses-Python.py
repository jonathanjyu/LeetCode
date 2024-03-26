#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def isValid(self, s):
    stack = []
    for i in s:
        if i in ['(','[','{']:
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
            elif i == ')' and stack[-1] == '(':
                stack.pop(-1)
            elif i == ']' and stack[-1] == '[':
                stack.pop(-1)
            elif i == '}' and stack[-1] == '{':
                stack.pop(-1)
            else:
                return False
        #print('stack :',stack)
    if len(stack) == 0:
        return True
    else:
        return False

