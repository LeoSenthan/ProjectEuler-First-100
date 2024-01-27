with open("022/#022.txt") as f:
    names=sorted(f.read().replace('"',"").split(","))
truetotal=0
for name in range(0,len(names)):
    total=0
    for char in names[name]:
        total=total+ord(char)-64
    total=total*(name+1)
    truetotal+=total
print(truetotal)