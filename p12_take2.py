def create_prime_list(x):
	primes = [2]
	a = 2
	while len(primes) < x:
		a = a + 1
		for entry in primes:
			if a % entry == 0:
				break
			if entry == primes[-1]:
				primes.append(a)
	return primes

primes = create_prime_list(2000)

def factors(n):
	f = 1
	x = n
	for e in primes:
		count = 0
		if e > n/2:
			break
		while x % e == 0:
			x = x / e
			count = count + 1
		f = f * (count + 1)
	return f

def triangle(divisors):
	triangle_number = 1
	natural_number = 1
	count = 0
	while count < divisors:
		natural_number = natural_number + 1
		triangle_number = triangle_number + natural_number
		count = factors(triangle_number)
	return triangle_number

print triangle(500)