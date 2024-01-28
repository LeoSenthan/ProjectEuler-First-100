triangles=[]
current=1
for i in range(0,50):
    current+=i
    triangles.append(current)
print(triangles)



with open("042/#042.txt") as f:
    names=f.read().split(",")
