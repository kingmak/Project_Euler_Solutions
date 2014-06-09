#Problem 1 Project Euler
Multiples = []
for num in range(0, 1000):
	if num % 3 == 0 or num % 5 == 0:
		Multiples.append(num)
print sum(Multiples)
