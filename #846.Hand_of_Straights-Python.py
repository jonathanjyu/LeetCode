#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    def checkInList(self,hand,tmp):
        j = 0 # run on tmp
        #print('hand:',hand)
        #print('tmp:',tmp)
        for i in range(len(hand)):
            if hand[i] == tmp[j]:
                hand[i] = -1
                j += 1
            if j == len(tmp):break
        #print('after:',hand)
        if j == len(tmp):return True
        else:return False


    def isNStraightHand(self, hand, groupSize):
        if len(hand) % groupSize != 0:return False
        hand = sorted(hand)
        tmp = [0]*len(hand)
        for i in range(len(hand)):
            if hand[i] != -1:
                tmp = list(range(hand[i],hand[i]+groupSize,1))
                check = self.checkInList(hand,tmp)
                if check == False:return False
        if max(hand) == -1 :return True
        else:return False

