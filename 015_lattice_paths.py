#Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
#How many such routes are there through a 20x20 grid?
#   _ _ _
#  |_|_|_|
#  |_|_|_|
#  |_|_|_|

def create_lattice(height,width):
	a = 0
	b = 0
	lattice = []
	while b <= height:
		lattice.append([])
		b = b + 1
	for e in lattice:
		a = 0
		while a <= width:
			e.append(0)
			a = a + 1
	return lattice

def solve_lattice(height,width):
	lattice = create_lattice(height,width)
	b = height
	while b >= 0:
		a = width
		while a >= 0:
			if b == height or a == width:
				lattice[b][a] = 1
			else:
				lattice[b][a] = lattice[b+1][a] + lattice[b][a+1]
			a = a - 1
		b = b - 1
	return lattice[0][0]

print solve_lattice(20,20)
