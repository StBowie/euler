#2 ** 15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#What is the sum of the digits of the number 2 ** 1000?

def sum_digits(n):
	a = str(n)
	sum = 0
	while len(a) <> 0:
		sum = sum + int(a[0])
		a = a[1:]
	return sum

print sum_digits(2 ** 1000)