'''
Sub-string divisibility
Problem 43
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

d2 d3 d4=406 is divisible by 2
d3 d4 d5=063 is divisible by 3
d4 d5 d6=635 is divisible by 5
d5 d6 d7=357 is divisible by 7
d6 d7 d8=572 is divisible by 11
d7 d8 d9=728 is divisible by 13
d8 d9 d10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.
'''
import itertools
def sub_string_divisibility():
	pandigitals = [''.join(p) for p in list(itertools.permutations('0123456789'))]
	return sum([int(p) for p in pandigitals
			if int(p[1:4]) % 2 == 0
			if int(p[2:5]) % 3 == 0
			if int(p[3:6]) % 5 == 0
			if int(p[4:7]) % 7 == 0
			if int(p[5:8]) % 11 == 0
			if int(p[6:9]) % 13 == 0
			if int(p[7:10]) % 17 == 0
			])

import time

def timedcall(fn,*args):
	t0 = time.clock()
	result = fn(*args)
	t1 = time.clock()
	return t1-t0, result

print timedcall(sub_string_divisibility)


