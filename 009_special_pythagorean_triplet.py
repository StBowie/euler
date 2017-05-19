#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#a2 + b2 = c2
#For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

def pyth_triplet(sum):
	a = 0
	b = 1
	while a < b:
		a = a + 1
		b = a + 1
		c = sum - b - a
		while b < c:
			if a ** 2 + b ** 2 == c ** 2:
				return [a,b,c],a * b * c
			b,c = b + 1, c - 1
	return "No such triplet"

print pyth_triplet(1000)