#https://en.wikipedia.org/wiki/Partition_(number_theory)#Generating_function
pentagonal=[1]
for i in range(1,250):
    pentagonal.append(int(i*(3*i-1)/2+i))
p,n,remainder=[1],0,[1, 1, -1, -1] # Sequence goes + + - - and keeps repeating in the formula
while p[n]>0:
    n+=1
    px, i = 0, 0
    while pentagonal[i]<=n:
        px+=p[int(n-pentagonal[i])]*remainder[i%4]
        i+=1
    p.append(px % 1000000)
print (n)