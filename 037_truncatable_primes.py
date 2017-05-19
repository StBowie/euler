'''
Truncatable primes
Problem 37
The number 3797 has an interesting property. Being prime itself,
it is possible to continuously remove digits from left to right,
and remain prime at each stage: 3797, 797, 97, and 7. Similarly
we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable
from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
'''

def trunc_primes(p):
	prime_list = [2]
	trunc_prime_list = []
	a = 2
	while len(trunc_prime_list) < p:
		a += 1
		for entry in prime_list:
			if a % entry == 0:
				break
			if entry == prime_list[-1]:
				prime_list.append(a)
				if trunc_prime_test(a,prime_list):
					trunc_prime_list.append(a)
	return trunc_prime_list

def trunc_prime_test(x,prime_list):
	if len(str(x)) < 2:
		return False
	for a in range(len(str(x))):
		if int(str(x)[a:]) not in prime_list:
			return False
	for b in range(1,len(str(x))):
		if int(str(x)[:-(b)]) not in prime_list:
			return False
	return True

print sum(trunc_primes(11))
