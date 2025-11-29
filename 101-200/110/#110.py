#1/x +1/y=1/n 
#n/x+n/y=1
#ny +nx = xy
#(x-n)(y-n)=n**2
#Number of solutions is number of divisors of n
#4 million = 2**8 * 5**6 hence number of primes is 15
#product of first 15 primes is 614889782588....
#log base 2 of this is roughly 60 
minimum = 614889782588491410
for a in range(1,60):
    print("a", a)
    b,c = (2*a + 1),2**a
    for d in range(1, 23):
        b,c = (2*a + 1)*(2*d + 1),2**a*3**d
        if c > minimum:
            break 
        for e in range(1,12):
            b,c = (2*a + 1)*(2*d + 1)*(2*e + 1),2**a * 3**d * 5**e
            if c > minimum:
                break
            for f in range(1,8):
                b,c = (2*a + 1)*(2*d + 1)*(2*e + 1)*(2*f + 1),2**a * 3**d * 5**e * 7**f
                if c > minimum:
                    break
                for g in range(1,6):
                    b,c = (2*a + 1)*(2*d + 1)*(2*e + 1)*(2*f + 1)*(2*g + 1),2**a * 3**d * 5**e * 7**f * 11**g
                    if c > minimum:
                        break
                    for h in range(4):
                        b,c = (2*a + 1)*(2*d + 1)*(2*e + 1)*(2*f + 1)*(2*g + 1)*(2*h + 1),2**a * 3**d * 5**e * 7**f * 11**g * 13**h
                        if c > minimum:
                            break
                        for i in range(4):
                            b,c = (2*a + 1)*(2*d + 1)*(2*e + 1)*(2*f + 1)*(2*g + 1)*(2*h + 1)*(2*i + 1),2**a * 3**d * 5**e * 7**f * 11**g * 13**h * 17**i
                            if c > minimum:
                                break
                            for j in range(3):
                                b,c = (2*a + 1)*(2*d + 1)*(2*e + 1)*(2*f + 1)*(2*g + 1)*(2*h + 1)*(2*i + 1)*(2*j + 1),2**a * 3**d * 5**e * 7**f * 11**g * 13**h * 17**i * 19**j
                                if c > minimum:
                                    break
                                for k in range(3):
                                    b,c = (2*a + 1)*(2*d + 1)*(2*e + 1)*(2*f + 1)*(2*g + 1)*(2*h + 1)*(2*i + 1)*(2*j + 1)*(2*k + 1),2**a * 3**d * 5**e * 7**f * 11**g * 13**h * 17**i * 19**j * 23**k
                                    if c > minimum:
                                        break
                                    for l in range(2):
                                        b,c = (2*a + 1)*(2*d + 1)*(2*e + 1)*(2*f + 1)*(2*g + 1)*(2*h + 1)*(2*i + 1)*(2*j + 1)*(2*k + 1)*(2*l + 1),2**a * 3**d * 5**e * 7**f * 11**g * 13**h * 17**i * 19**j * 23**k * 29**l
                                        if c > minimum:
                                            break
                                        for m in range(2):
                                            b,c = (2*a + 1)*(2*d + 1)*(2*e + 1)*(2*f + 1)*(2*g + 1)*(2*h + 1)*(2*i + 1)*(2*j + 1)*(2*k + 1)*(2*l + 1)*(2*m + 1),2**a * 3**d * 5**e * 7**f * 11**g * 13**h * 17**i * 19**j * 23**k * 29**l * 31**m
                                            if c > minimum:
                                                break
                                            for n in range(2):
                                                b,c = (2*a + 1)*(2*d + 1)*(2*e + 1)*(2*f + 1)*(2*g + 1)*(2*h + 1)*(2*i + 1)*(2*j + 1)*(2*k + 1)*(2*l + 1)*(2*m + 1)*(2*n + 1),2**a * 3**d * 5**e * 7**f * 11**g * 13**h * 17**i * 19**j * 23**k * 29**l * 31**m * 37**n
                                                if c > minimum:
                                                    break
                                                for o in range(2):
                                                    b,c = (2*a + 1)*(2*d + 1)*(2*e + 1)*(2*f + 1)*(2*g + 1)*(2*h + 1)*(2*i + 1)*(2*j + 1)*(2*k + 1)*(2*l + 1)*(2*m + 1)*(2*n + 1)*(2*o + 1),2**a * 3**d * 5**e * 7**f * 11**g * 13**h * 17**i * 19**j * 23**k * 29**l * 31**m * 37**n * 41**o
                                                    if b > 8*10**6 and c < minimum:
                                                        minimum = c
print(minimum)