#NOT EFFICIENT AT ALL
pentagonal,n=[1,5,12,22,35,51,70,92,117,145],10
while True:
    n+=1
    pentagonal.append(int(n*(3*n-1)/2))
    if pentagonal[-1]>100000000:
        break
for num1 in range(0,len(pentagonal)):
    for num2 in range(0,num1):
        if pentagonal[num2]-pentagonal[num1] in pentagonal:
            if pentagonal[num2]+pentagonal[num1] in pentagonal:
                print(pentagonal[num1],pentagonal[num2],pentagonal[num2]-pentagonal[num1])
                exit()