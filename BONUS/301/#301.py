#Pattern when n**a is fibbonaci sequence so n**3 = 3rd fibbonaci number
fib=[1,1]
for i in range(0,32):
    fib.append(fib[-1]+fib[-2])
print(fib[31])