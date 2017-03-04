'''
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide
evenly into n).
If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of
a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''

import math

def d(n):
    if n < 2:
        return 0
    sum = 1
    i = 2
    while i < math.sqrt(n):
        if n % i == 0:
            sum += i + n/i
        i += 1
    if n != 1 and math.sqrt(n) % 1 == 0:
        sum += math.sqrt(n)
    return sum

def amicable_numbers_sum(max):
    amicable_num = []
    a = 1
    sum = 0
    while a < max:
        if d(a) != d(d(a)) and a == d(d(a)) and a not in amicable_num and d(a) < max:
            sum += a + d(a)
            amicable_num.append(a)
            amicable_num.append(d(a))
        a += 1
    return sum,amicable_num

print amicable_numbers_sum(10000)