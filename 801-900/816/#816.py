points=[[290797,290797**2%50515093]]
while len(points)<15:
    x=points[-1][-1]**2%50515093
    y=x**2%50515093
    points.append([x,y])
print(points)