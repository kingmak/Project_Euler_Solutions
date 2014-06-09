#Problem 4 Project Euler
palindrome = 0
for numOne in range(100, 1000):
	for numTwo in range(100, 1000):
		numba = numOne * numTwo
		if str(numba) == str(numba)[::-1]:
			if numba > palindrome:
					palindrome = numba
print 'larger palindrom = %d ' % palindrome
