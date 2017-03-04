#Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

def sum_digits_powers(power):
	result = []
	summation = 0
	for x in range(10,1000000):
		total = 0
		for y in str(x):
			total += int(y) ** power
		if x == total:
			result.append(x)
			summation += x
	return summation,result

print sum_digits_powers(5)