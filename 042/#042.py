triangles,current,triangletotal=[1],1,0
for i in range(2,60):
    current+=i
    triangles.append(current)

with open("042/#042.txt") as f:
    names=f.read().split(",")

for name in names:
    name,total=name.replace('"',""),0
    for char in name:
        total+=ord(char)-64
    if total in triangles:
        triangletotal+=1
print(triangletotal)
