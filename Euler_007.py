def isPrime(n):
    return n > 1 and all(n % i for i in range(2, int(n ** 0.5) + 1))  

index = 2
primes = []

while len(primes) != 10001:
    if isPrime(index):
        primes.append(index)
    index += 1
print primes[-1]