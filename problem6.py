# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 18:05:29 2017

@author: harne
"""

    hand = None
    userInput = ''
    while(userInput != 'e'):
        userInput = input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ').lower()
        if(userInput == 'n'):
            playerInput = input('Enter u to have yourself play, c to have the computer play: ').lower()
            hand = dealHand(HAND_SIZE)
            if(playerInput == 'c'):
                compPlayHand(hand, wordList, HAND_SIZE)
            else:
                playHand(hand, wordList, HAND_SIZE)
        elif(userInput == 'r'):
            playerInput = input('Enter u to have yourself play, c to have the computer play: ').lower()
            if(hand != None):
                hand = dealHand(HAND_SIZE)
                if(playerInput == 'c'):
                    compPlayHand(hand, wordList, HAND_SIZE)
                else:
                    playHand(hand, wordList, HAND_SIZE)
            else:
                print("You have not played a hand yet. Please play a new hand first!")
        elif(userInput == 'e'):
            break
        else:
            print("Invalid command.")