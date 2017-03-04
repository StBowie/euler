#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 10:04:04 2017
#
A perfect number is a number for which the sum of its proper divisors is exactly
equal to the number. For example, the sum of the proper divisors of 28 would be
1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n
and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number
that can be written as the sum of two abundant numbers is 24. By mathematical
analysis, it can be shown that all integers greater than 28123 can be written
as the sum of two abundant numbers. However, this upper limit cannot be reduced
any further by analysis even though it is known that the greatest number that
cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of
two abundant numbers.

"""

import math

def d(n):
    if n < 2:
        return 0
    sum = 1
    i = 2
    while i < math.sqrt(n):
        if n % i == 0:
            sum += i + n/i
        i += 1
    if n != 1 and math.sqrt(n) % 1 == 0:
        sum += math.sqrt(n)
    return sum

def abundant_numbers(max):
    n = 1
    list = []
    for n in range(1,max):
        if d(n) > n:
            list.append(n)
    return list

def non_abundant_sum_test(x,list):
    for entry in list:
        e = x - entry
        if e in list and entry + e == x:
            return False
        if entry > x/2.0:
            break
    return True

def non_abundant_sums(max):
    sum = 0
    list = abundant_numbers(max)
    for n in range(0,max):
        if non_abundant_sum_test(n,list):
            sum += n
    return sum
    
print non_abundant_sums(28123)

