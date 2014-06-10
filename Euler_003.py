#
x, num = 2, 600851475143
while num != x:
    if num % x == 0: num = num / x; x = 2
    else: x += 1
print x
