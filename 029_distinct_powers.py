#How many distinct terms are in the sequence generated by a**b for 2 <= a <= 100 and 2 <= b <= 100?

def distinct_powers(x,y):
	result = []
	for a in range(2,x+1):
		for b in range(2,y+1):
			result.append(a**b)
	return len(sorted(set(result)))

print distinct_powers(100,100)

'''
#attempted list comprehension
def distinct_powers1(x,y):
	return len(set([a**b for a,b in range(2,x+1),range(2,y+1)]))

print distinct_powers1(5,5)
'''