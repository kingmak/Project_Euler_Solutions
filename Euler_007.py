'''
def isPrime(n):
    return n > 1 and all(n % i for i in range(2, int(n ** 0.5) + 1))  

index = 2
primes = []

while len(primes) != 10001:
    if isPrime(index):
        primes.append(index)
    index += 1
print primes[-1]
'''

def isPrime(n):
    # if n <= 1: return False
    # if n <= 3: return True

    if (n % 2 == 0) or (n % 3 == 0):
        return False

    index = 5
    while (index * index) <= n:
        if (n % index == 0) or ((n % (index + 2)) == 0):
            return False
        index += 6

    return True

index = 3
primes = [2, 3] # added 2 since its the only even prime

while len(primes) != 10001:
    if isPrime(index):
        primes.append(index)
    index += 2
print primes[-1]