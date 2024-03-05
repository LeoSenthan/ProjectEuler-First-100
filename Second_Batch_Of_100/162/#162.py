#https://en.wikipedia.org/wiki/Inclusion%E2%80%93exclusion_principle
sum=0
for k in range(3,17):
    sum=sum+15*16**(k-1)-2*14*15**(k-1)-15**k+13*14**(k-1)+2*14**k-13**k
print(str(hex(sum)))