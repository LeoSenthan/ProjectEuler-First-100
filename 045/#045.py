#All hexagonal numbers are triangle numbers hence only need to check hexagonal numbers to pentagonal numbers
hexagonal,pentagonal,n=[],[],0
while True:
    n+=1
    hexagonal.append(n*(2*n-1))
    pentagonal.append(int(n*(3*n-1)/2))
    if pentagonal[-1] in hexagonal:
        if pentagonal[-1]>40755:
            print(pentagonal[-1])
            exit()