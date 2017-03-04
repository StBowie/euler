#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

#What is the 10,001st prime number?


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

print create_prime_list(10001)[-1]