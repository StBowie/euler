'''
If a box contains twenty-one coloured discs, composed of fifteen blue discs and six red discs,
and two discs were taken at random, it can be seen that the probability of taking two blue discs,
P(BB) = (15/21)*(14/20) = 1/2.

The next such arrangement, for which there is exactly 50% chance of taking two blue discs at random,
is a box containing eighty-five blue discs and thirty-five red discs.

By finding the first arrangement to contain over 10**12 = 1,000,000,000,000 discs in total, determine
the number of blue discs that the box would contain.'''

#INCORRECT

import math

def prob(start,end,target_p):
	for total_discs in range(max(2,start),end):
		blue_discs = 1.0*math.ceil(math.sqrt(target_p)*total_discs)
		if blue_discs*(blue_discs-1)/total_discs/(total_discs-1) == target_p:
			return blue_discs,total_discs
	return "Not working!"

print prob(10**12,10**12 + 10**4,.5)
"707106783028"