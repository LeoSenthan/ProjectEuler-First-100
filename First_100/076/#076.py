ways=[1]+[0]*100 # Number of ways to make 1 is 1 so create the list 
for n in range(1,100):
    for i in range(n, 101):
        ways[i] += ways[i-n]
print (ways,ways[100])