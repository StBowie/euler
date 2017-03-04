'''
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
'''
def diagonal(width):
	total = 1
	for a in range(3,width+1,2):
		total += 4 * (a ** 2) - 6 * (a-1)
	return total

print diagonal(1001)

'''
#trying to limit to one line
def diagonal1(width): return reduce(sum,[1] + [(4 * a**2 -6*(a-1)) for a in range(3,width+1,2)])

print diagonal1(5)
'''