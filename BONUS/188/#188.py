start=1
for i in range(1855):    
    next=pow(1777,start,10**8)
    if start==next:
        break
    start=next
print(next)