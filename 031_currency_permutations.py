'''
1p, 2p, 5p, 10p, 20p, 50p, 100p and 200p.

How many different ways can 200p be made using any number of coins?
'''

def currency_combinations(target):
	result = []
	for a in range(target/1 + 1):
		for b in range((target - a)/2 + 1):
			for c in range((target - a - 2*b)/5 + 1):
				for d in range((target - a - 2*b - 5*c)/10 + 1):
					for e in range((target - a - 2*b - 5*c - 10*d)/20 + 1):
						for f in range((target - a - 2*b - 5*c - 10*d - 20*e)/50 + 1):
							for g in range((target - a - 2*b - 5*c - 10*d - 20*e - 50*f)/100 + 1):
								for h in range((target - a - 2*b - 5*c - 10*d - 20*e - 50*f - 100*g)/200 + 1):
									if 1*a + 2*b + 5*c + 10*d + 20*e + 50*f + 100*g + 200*h == target:
										result.append((a,b,c,d,e,f,g,h))
	return result

print len(currency_combinations(200))