'''
There are exactly ten ways of selecting three from five, 12345:
123, 124, 125, 134, 135, 145, 234, 235, 245, and 345
In combinatorics, we use the notation, 5C3 = 10.
It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.
How many, not necessarily distinct, values of  nCr, for 1 <= n <= 100, are greater than one-million?
'''

import math

def nCr(n,r):
	return math.factorial(n)/(math.factorial(r)*math.factorial(n-r))

print len([(n,r) for n in range(1,101) for r in range(1,n+1)if nCr(n,r) >1000000])