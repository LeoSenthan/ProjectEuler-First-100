#Max value for digit = 9**5=59049
#Hence max possible is 6 digits as 7 digits max value is only 413343
totalsum=0
for n in range(2,1000000):
    digits,total=str(n),0
    for digit in digits:
        total+=int(digit)**5
    if total==n:
        totalsum+=total
print(totalsum)