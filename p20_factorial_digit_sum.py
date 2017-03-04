#For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800,
#and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

#Find the sum of the digits in the number 100!

def factorial(n):
	count = n
	while n > 1:
		n += -1
		count = count * n
	return count

def sum_digits(n):
	sum = 0
	a = str(n)
	for e in a:
		sum += int(e)
	return sum

print sum_digits(factorial(100))