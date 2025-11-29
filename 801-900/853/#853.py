fibbonaci=[1,1]
while fibbonaci[-1]<1000000000:
    fibbonaci.append(fibbonaci[-1]+fibbonaci[-2])
print(fibbonaci)
result=[]
for number in fibbonaci[1:]:
    result.append(number%19)
print(result)