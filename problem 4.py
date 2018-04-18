# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 14:50:15 2017

@author: harne
"""

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    # TO DO... <-- Remove this comment when you code this function
    values = list(hand.values())
    result = 0
    for i in range(len(values)):
        result += values[i]
    return result    


hand = {'r': 1, 'a': 3, 'p': 2, 'e': 1, 't': 1, 'u': 1}

print(calculateHandlen(hand))