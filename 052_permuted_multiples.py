#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 12:28:34 2017

@author: sbowie
"""
'''
It can be seen that the number, 125874, and its double, 251748, contain exactly
the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
contain the same digits.
'''

def permuted_multiples(start,stop):
    x = start
    while x < stop:
        x += 1
        if multiples_test(x,6) and multiples_test(x,5) and multiples_test(x,4) and multiples_test(x,3) and multiples_test(x,2):
            return x
    return "Not found"

def multiples_test(x,multiple):
    x,y = str(x),str(multiple * x)
    for a in x:
        count = 0
        for b in y:
            if a == b:
                count += 1
            if b not in x:
                return False
        if count != 1:
            return False
    return True

print permuted_multiples(1,10**7)
print [142857*x for x in range(1,6)]