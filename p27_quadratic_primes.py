#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 11:06:46 2017

@author: sbowie
"""
'''
Euler discovered the remarkable quadratic formula:

n**2+n+41

It turns out that the formula will produce 40 primes for the consecutive integer
values 0≤n≤39.
However, when n=40,40**2+40+41 = 40(40+1)+41 is
divisible by 41, and certainly when n=41,41**2+41+41 is clearly
divisible by 41.

The incredible formula n**2−79n+1601 was discovered, which produces
80 primes for the consecutive values 0≤n≤79. The product of the
coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n2+an+b, where |a|<1000 and |b|≤1000

where |n| is the modulus/absolute value of n

e.g. |11|=11 and |−4|=4

Find the product of the coefficients, a and b, for the quadratic expression
that produces the maximum number of primes for consecutive values of n,
starting with n=0.
'''

import math

def primes(x):
    p_list = []
    for n in range(2,x):
        prime = True
        for a in p_list:
            if a > math.sqrt(n):
                break
            if n % a == 0:
                prime = False
                break
        if prime:
            p_list.append(n)
    return p_list

p_list = primes(10000)

def quadratic_primes(primes,abs_a,abs_b):
    best = (0,0,0)
    for a in range(-(abs_a-1),abs_a):
        for b in range(-(abs_b),(abs_b+1)):
            n = 0
            while n**2 + a * n + b in primes:
                n += 1
            test = (n - 1,a,b,(n-1)**2 + a * (n-1) + b)
            if test > best:
                best = test
    return best
            
print quadratic_primes(p_list,1000,1000)
            
            