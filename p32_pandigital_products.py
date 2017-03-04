#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 11:06:46 2017

@author: sbowie
"""
'''
We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1
through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity
can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only
include it once in your sum.
'''

from itertools import permutations
p = [''.join(p) for p in permutations('123456789')]

def pandigital_product(perms):
    result, sum = [],0
    for perm in perms:
        if int(perm[0]) * int(perm[1:5]) == int(perm[5:]) or int(perm[:2]) * int(perm[2:5]) == int(perm[5:]):
            if perm[5:] not in result:
                result.append(perm[5:])
                sum += int(perm[5:])
    return result, sum

print pandigital_product(p)
