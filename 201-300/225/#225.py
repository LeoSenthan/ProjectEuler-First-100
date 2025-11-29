count, i = 0, 27
while count < 124:
    trib1, trib2, trib3 = 1, 1, 3
    while trib3>0 and trib1 * trib2 * trib3 != 1:
        trib1, trib2, trib3 = trib2, trib3, (trib1 + trib2 + trib3) % i
    if trib3>0: 
        count+=1
    i+=2
print(i-2)