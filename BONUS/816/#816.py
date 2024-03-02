points=[290797]
while len(points)!=15:
    points.append((points[-1]**2)%50515093)
points=sorted(points)
for i in range(0,len(points)-1):
    print(points[i+1]-points[i])
    