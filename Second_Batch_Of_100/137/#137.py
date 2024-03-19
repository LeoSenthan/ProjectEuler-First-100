#searched sequence up https://oeis.org/A081018
#Golden Nugget = Fibbonaci(2n)*Fibbonaci(2n+1)
# 15th Golden Nugget = Fibbonaci(30)*Fibbonaci(31)
fibbonaci=[1,1]
while len(fibbonaci)<31:
    fibbonaci.append(fibbonaci[-1]+fibbonaci[-2])
print(fibbonaci[-1]*fibbonaci[-2])