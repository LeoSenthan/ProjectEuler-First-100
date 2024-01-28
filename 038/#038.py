# Minimum to beat is 918273645 hence first product has to start with 9
max=0
for number in range(1,10000): # As n>1 Maximum number to start with is 9999
    string=str(number)
    n=1
    while len(string)<9:
        n+=1
        string+=str(number*n)
    if len(string)!=9:
        pass
    else:
        pandigital=list(set(string))
        if "0" not in pandigital and len(pandigital)==9:
            if int(string)>max:
                max=int(string)
print(max)