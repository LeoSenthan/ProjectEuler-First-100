with open("018/#018.txt","r") as f:
    triangle=f.readlines()
for row in range(0,len(triangle)):
    triangle[row]=triangle[row].replace("\n","").split(" ")
triangle.reverse()
for layer in range(0,len(triangle)):
    for number in range(0,len(triangle[layer])-1):
        if int(triangle[layer][number])>int(triangle[layer][number+1]):
            triangle[layer+1][number]=int(triangle[layer+1][number])+int(triangle[layer][number])
        else:
            triangle[layer+1][number]=int(triangle[layer+1][number])+int(triangle[layer][number+1])
print(triangle[-1])
#integer conversions make algorithm slightly inefficient