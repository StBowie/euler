#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 22:00:24 2017

@author: sbowie
"""
'''
In the card game poker, a hand consists of five cards and are ranked, from
lowest to highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest
value wins; for example, a pair of eights beats a pair of fives (see example 1
below). But if two ranks tie, for example, both players have a pair of queens,
then highest cards in each hand are compared (see example 4 below); if the
highest cards tie then the next highest cards are compared, and so on.

The file, poker.txt, contains one-thousand random hands dealt to two players.
Each line of the file contains ten cards (separated by a single space): the
first five are Player 1's cards and the last five are Player 2's cards. You
can assume that all hands are valid (no invalid characters or repeated cards),
each player's hand is in no specific order, and in each hand there is a clear
winner.

How many hands does Player 1 win?
'''

with open('p054_poker.txt') as f:
    hands = f.readlines()
    hands = [x.strip() for x in hands] 
    hands = [[x[:14].split(), x[15:].split()] for x in hands]

def poker(hands):
    "Return a list of winning hands: poker([hand,...]) => [hand,...]"
    return allmax(hands, key=hand_rank)

def allmax(iterable, key=None):
    "Return a list of all items equal to the max of the iterable."
    result, best = [], None
    key = key or (lambda x: x)
    for x in iterable:
        xval = key(x)
        if not result or xval > best:
            result, best = [x], xval
        elif xval == best:
            result.append(x)
    return result

def hand_rank(hand):
    "return a value indicating how high the hand ranks"
    #counts is the count of each rank; ranks lists corresponding ranks
    #E.g. '7 T 7 9 7' => counts = (3,1,1); ranks = (7,10,9)
    groups = group(['--23456789TJQKA'.index(r) for r,s in hand])
    counts, ranks = unzip(groups)
    if ranks == (14,5,4,3,2):
        ranks = (5,4,3,2,1)
    straight = len(ranks) == 5 and max(ranks) - min(ranks) == 4
    flush = len(set([s for r,s in hand])) == 1
    return max(count_rankings[counts],4*straight + 5*flush),ranks

count_rankings = {(5,):10,(4,1):7,(3,2):6,(3,1,1):3,(2,2,1):2,(2,1,1,1):1,(1,1,1,1,1):0}

def unzip(x):
    return zip(*x)

def group(items):
    "return a list of [(count,x)...] highest count first, then highest x first"
    groups = [(items.count(x),x) for x in set(items)]
    return sorted(groups, reverse=True)

def poker_winner(list):
    player1, player2,tie = 0,0,0
    for hand in list:
        if poker(hand) == [hand[0]]:
            player1 += 1
        elif poker(hand) == [hand[1]]:
            player2 += 1
        else:
            tie += 1
    return "Player 1: ", player1, "Player 2: ", player2, "Tie: ", tie

print poker_winner(hands)




