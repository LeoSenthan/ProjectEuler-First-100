from itertools import permutations
total=0
perms=permutations(["0","1","2","3","4","5","6","7","8","9"])
for number in perms:
    string=""
    for digit in number:
        string+=digit
    if int(string)>987654321:
        if int(string[1:4])%2==0:
            if int(string[2:5])%3==0:
                if int(string[3:6])%5==0:
                    if int(string[4:7])%7==0:
                        if int(string[5:8])%11==0:
                            if int(string[6:9])%13==0:
                                if int(string[7:10])%17==0:
                                    total+=int(string)
print(total)