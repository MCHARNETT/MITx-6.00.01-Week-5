# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 14:23:59 2017

@author: harne
"""

def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    newHand = hand.copy()
    for i in range(len(word)):
        if word[i] in newHand.keys():
            newHand[word[i]] -=1
    
    return newHand