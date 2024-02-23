from decimal import Decimal, getcontext
getcontext().prec = 102  #Precision now 102 since the next 2 digits can affect the 100th digit
total = 0
for n in range(2, 100):
    root=str(Decimal(n).sqrt())
    if int(root) % 1 != 0:
        root_str = root[:101].replace(".","")    
        total += sum(int(c) for c in root_str)
print(total)
