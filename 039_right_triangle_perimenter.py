'''
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c},
there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p <= 1000, is the number of solutions maximised?
'''

def right_triangle_sides(perimeter):
	solutions = []
	for a in range(1,perimeter):
		for b in range(a,perimeter):
			if a**2 + b**2 == (perimeter - a - b)**2:
				solutions.append((a,b,(perimeter - a - b)))
			elif a**2 + b**2 >= (perimeter - a - b)**2:
				break
	return len(solutions)

print right_triangle_sides(120)

def max_triangle_solutions(max_perimeter):
	return max([x for x in range(max_perimeter+1)],key=right_triangle_sides)

print max_triangle_solutions(1000)