#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?

def prime_factors(start,end):
	list = []
	if start <= 2:
		factor = 2
	else:
		factor = start
	x = end
	while factor <= x:
		if x % factor == 0:
			list.append(factor)
		while x % factor == 0:
			x = x / factor
		if x == 1:
			return list
		else:
			factor = factor + 1
	list.append(x)
	return list

def biggest_prime_factor(x):
	factor = 2
	while factor < x:
		while x % factor == 0:
			x = x / factor
		if x == 1:
			return factor
		else:
			factor = factor + 1
	return x

print biggest_prime_factor(600851475143)