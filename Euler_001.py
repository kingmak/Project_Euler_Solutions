#Problem 1 Project Euler
Multiples = 0
for num in range(0, 1000):
	if num % 3 == 0 or num % 5 == 0: Multiples += num
print Multiples
