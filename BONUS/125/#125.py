#max square=10**8
total,correct=0,[]
squares=[square**2 for square in range(1,10001)]
for current in range(0,len(squares)):
    sum=squares[current]
    next=current
    while sum<10**8:
        next+=1
        sum+=squares[next]
        if str(sum)==str(sum)[::-1] and str(sum) not in correct:
            total+=sum
            correct.append(str(sum))
print(total)