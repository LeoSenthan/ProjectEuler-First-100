total,layer=1,1
while layer<1001:
    layer+=2
    max=layer**2
    total+=4*max-(layer-1)*6
print(total)