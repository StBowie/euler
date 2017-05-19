def fibonacci_length(length):
	current = 0
	after = 1
	index = 0
	while len(str(current)) < length:
		current,after = after,current + after
		index += 1
	return index

print fibonacci_length(1000)