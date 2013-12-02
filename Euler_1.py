#Problem 1 Project Euler
from collections import OrderedDict

def FindMultiples(num, Array):
    count = 0
    while count < len(NumStorage):
        if NumStorage[count] % num == 0:
            Array.append(NumStorage[count])
        count += 1
        
NumStorage = list(range(0, 1000))
Num3s = []; Num5s = []; SumMultiples = []
                             
FindMultiples(3, Num3s); FindMultiples(5, Num5s)

SumMultiples = Num3s + Num5s
SumMultiples = list (OrderedDict.fromkeys(SumMultiples))
SumMultiples = sum(SumMultiples)

print 'The Sum of the Multiples of 3 and 5 Between 0 to 1000 is:\n' + str(SumMultiples)
raw_input('')
