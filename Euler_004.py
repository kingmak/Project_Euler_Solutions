#Problem 4 Project Euler
palindrome = 0
for x in range(100, 1000):
	for y in range(100, 1000):
		num = x * y
		if str(num) == str(num)[::-1]: 
			if num > palindrome: palindrome = num
print 'largest Palindrome Number = %d ' % palindrome
