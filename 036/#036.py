# Only need to check odd numbers since if even final bit is a 0 hence will not be palindromic
total=0
for n in range(1,1000000,2):
    if str(n)==str(n)[::-1]:
        binary=str(bin(n))[2:]
        if binary==binary[::-1]:
            total+=n
print(total)
        