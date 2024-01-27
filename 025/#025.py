prev,current,count=1,1,2
while len(str(current))<1000:
    current,prev,count=prev+current,current,count+1
print(count)
