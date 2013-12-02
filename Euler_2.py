#Problem 2 Project Euler
FiboNums = []
FiboEvenNums = []

def FiboSeq(end):
    first, second = 0, 1
    while second < end:
        FiboNums.append(second)
        first, second = second, first + second

def Comparison():
    count = 0
    while count < len(FiboNums):
        if FiboNums[count] % 2 == 0:
            FiboEvenNums.append(FiboNums[count])
        count += 1

FiboSeq(4000000)
Comparison()
print sum(FiboEvenNums)
raw_input('')
