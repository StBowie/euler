#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

#Find the sum of all the multiples of 3 or 5 below 1000.

def list_multiples(base,max):
	list = []
	multiple = base
	while multiple < max:
		list.append(multiple)
		multiple = multiple + base
	return list

def union(list1,list2):
	for e in list2:
		if e not in list1:
			list1.append(e)
	return list1

print sum(union(list_multiples(3,1000),list_multiples(5,1000)))