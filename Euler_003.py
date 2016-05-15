#Problem 3 Project Euler
x, num = 2, 600851475143
while num != x:
    if num % x == 0: num = num / x
    x += 1
print x
