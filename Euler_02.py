#Problem 2 Project Euler
FiboNums = []
first, second, end = 0, 1, 4000000
while second < end:
    if second % 2 == 0:
    	FiboNums.append(second)
    first, second = second, first + second
print sum(FiboNums)
