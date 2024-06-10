#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    def replaceWords(self, dictionary, sentence):
        sentence = sentence.split()
        #print(sentence)
        for i in range(len(sentence)):
            for j in range(len(dictionary)):
                #print(sentence[i][0:len(dictionary[j])])
                #print(dictionary[j])
                if sentence[i][0:len(dictionary[j])] == dictionary[j]:
                    sentence[i] = dictionary[j]
        return ' '.join(sentence)

