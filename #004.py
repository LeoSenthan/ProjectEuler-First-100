#004
max=0
for multiple1 in range(999,99,-1):
    for multiple2 in range(999,99,-1):
        product=str(multiple1*multiple2)
        if product==product[::-1]:
            if max<int(product):
                max=int(product)
print(max)