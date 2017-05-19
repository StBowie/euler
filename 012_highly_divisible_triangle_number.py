def triangle(divisors):
	triangle_numbers = [1]
	natural_numbers = [1]
	count = 0
	a = 1
	while count < divisors:
		count = 0
		if len(natural_numbers) <= a + 1 or natural_numbers[-1] < triangle_numbers[-1] + natural_numbers[a]:
			natural_numbers.append(natural_numbers[-1] + 1)
		else:
			triangle_numbers.append(triangle_numbers[-1] + natural_numbers[a])
			a = a + 1
			if triangle_numbers[-1] % 2 == 0 and triangle_numbers[-1] % 3 == 0 and triangle_numbers[-1] % 5 == 0 and triangle_numbers[-1] % 7 == 0:
				for e in natural_numbers:
					if triangle_numbers[-1] % e == 0:
						count = count + 1
	return triangle_numbers[-1]

print triangle(500)