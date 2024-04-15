#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def uniqueMorseRepresentations(self, words):
    letter = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    letter_map = {}

    for i in range(len(letter)):
        letter_map[letter[i]] = code[i]
    ans_set = set()
    for i in range(len(words)):
        tmp = ""
        for j in range(len(words[i])):
            tmp = tmp + letter_map[words[i][j]]
        if tmp not in ans_set:
            ans_set.add(tmp)
    return len(ans_set)

