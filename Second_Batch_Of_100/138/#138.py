#17 and 305 are half of fibbonaci (9) and fibbonaci(19) hence probably is a sequence of every 6th element starting from 9 halved
fibbonaci=[1,1]
while len(fibbonaci)<1000:
    fibbonaci.append(fibbonaci[-1]+fibbonaci[-2])
    
print(sum(fibbonaci[6*n+2]/2 for n in range(1,13)))