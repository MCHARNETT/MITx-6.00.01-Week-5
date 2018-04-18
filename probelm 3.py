# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 14:34:32 2017

@author: harne
"""

def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    newHand = hand.copy()
    word = word.lower()
    for i in range(len(word)):
        if word[i] not in newHand:
            return False
        else:
            newHand[word[i]] -=1
    if word in wordList:
        return True
    
    return False

WORDLIST_FILENAME = "words.txt"
print(isValidWord("rapture", hand, ))
Expected False, but got True for word: 'rapture' and hand: {'r': 1, 'a': 3, 'p': 2, 'e': 1, 't': 1, 'u': 1}