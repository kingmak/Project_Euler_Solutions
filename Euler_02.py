#Problem 2 Project Euler
FiboNumSum = 0
first, second, end = 0, 1, 4000000
while second < end:
    if second % 2 == 0:
    	FiboNumSum += second
    first, second = second, first + second
print FiboNumSum
