#answer is a multiple of primes 2*3*5*7*11*13*17*19*23
#first and last are always resilient
count=0
for n in range(1,(8*3*5*7*11*13*17*19*23),2):
        if n%3!=0:
            if n%5!=0:
                if n%7!=0:
                    if n%11!=0:
                         if n%13!=0:
                              if n%17!=0:
                                   if n%23!=0:
                                        count+=1
print(count/(8*3*5*7*11*13*17*19*23))
print(8*3*5*7*11*13*17*19*23)
#tried multiples of this got lucky