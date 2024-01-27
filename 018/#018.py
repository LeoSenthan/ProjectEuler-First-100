with open("018/#018.txt","r") as f:
    triangle=f.readlines()
for row in range(0,len(triangle)):
    triangle[row]=triangle[row].replace("\n","").split(" ")
    print(triangle[row])
for layer in range(len(triangle),0,-1):
    for number in range(0,len(triangle[layer])):
        pass