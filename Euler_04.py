#Problem 4 Project Euler

Palindromes = []
Products = []

def FindProducts():
        global Products
        for i in range (100, 1000):
                for j in range (100, 1000):
                        Products.append(i * j)
                        j += 1
                i += 1

def FindPalindromes():
        count = 0
        while count < len(Products):
                if str(Products[count]) == str(Products[count])[::-1]:
                        Palindromes.append(Products[count])
                count += 1
                
FindProducts()
FindPalindromes()
LenPalindromes = len(Palindromes)
LargestPalindrome =  sorted(Palindromes)[LenPalindromes - 1]
print LargestPalindrome
raw_input('')
