#002
prev,current,list=1,1,[]
while current<4000000:
    if current%2==0:
        list.append(current)
    prev,current=current,current+prev
print(sum(list))