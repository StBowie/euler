#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.

import math

def sum_of_primes(max):
	primes = [2]
	a = 3
	sum = 2
	while a < max:
		for entry in primes:
			if a % entry == 0:
				break
			if entry > math.sqrt(a):
				primes.append(a)
				sum = sum + a
				break
		a = a + 2
	return sum

print sum_of_primes(2000000)