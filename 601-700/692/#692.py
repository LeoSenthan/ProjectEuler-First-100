#This is Fibbonaci Nim Game Disguised
#If starting number is fibbonaci then minimum start is all of them
#Zeckendorf Representation 
#https://en.wikipedia.org/wiki/Fibonacci_nim
fibonacci = [1, 2]
while fibonacci[-1] <= 23416728348467685:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])
fibbonaci=fibonacci[:-1]

def zeckendorf_representation(n,fibbonaci):
    zeckendorf = []
    i = len(fibonacci) - 1  # Start from the largest Fibonacci number
    while n > 0:
        if fibonacci[i] <= n:
            zeckendorf.append(fibonacci[i])
            n -= fibonacci[i]
        i -= 1
    return zeckendorf
#if the maximum possible number of coins removed from current number is greater or equal to smallest fibbonaci number in expression that player wins