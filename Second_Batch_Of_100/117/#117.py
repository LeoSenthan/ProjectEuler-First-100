# ways(n) = ways(n-1)+ ways(n-2)+ways(n-3)+ways(n-4)
ways=[0,0,0,0,1]
while len(ways)!=55:
    ways.append(ways[-1]+ways[-2]+ways[-3]+ways[-4])
print(ways[-1])