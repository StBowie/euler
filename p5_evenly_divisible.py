#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def build_integer_list(start,end):
	list = []
	while start <= end:
		list.append(start)
		start = start + 1
	return list

def multiply_list(list):
	result = 1
	for e in list:
		result = result * e
	return result

def test_evenly_divisible(x,list):
	for e in list:
		if x % e <> 0:
			return False
	return True

def simplify(x,list):
	while 1 in list:
		list.remove(1)
	for e in list:
		while test_evenly_divisible(x,list):
			x = x / e
		if not test_evenly_divisible(x,list):
			x = x * e
	return x

print simplify(multiply_list(build_integer_list(1,20)),build_integer_list(1,20))


#if a larger number is the product of two smaller numbers in the list, which are not squares of each other, the larger number is redundant
#if a larger number is the square of a smaller number, the smaller number is redundant