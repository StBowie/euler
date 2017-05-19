#Find the largest palindrome made from the product of two 3-digit numbers.

def test_palindrome(x):
	return x == x[::-1]

def largest_palindrome(max_factor,min_factor):
	palindrome = []
	used_factors = []
	x = max_factor
	y = max_factor
	z = min_factor
	while x > z:
		while y > z:
			if test_palindrome(str(x * y)):
				palindrome.append(x * y)
				used_factors.append([x,y])
				z = y
			else:
				y = y - 1
		x = x - 1
		y = x
	return max(palindrome), palindrome, used_factors

print largest_palindrome(999,100)