months=[31,28,31,30,31,30,31,31,30,31,30,31]
leapmonths=[31,29,31,30,31,30,31,31,30,31,30,31]
day=1
year=1900
fullcount=0
while year<2001:
    count=0
    if year%400==0:
        use=leapmonths
    elif year%100==0:
        use=months
    elif year%4==0:
        use=leapmonths
    else:
        use=months
    for month in range(0,len(use)):
        day=day+use[month]
        if day%7==0:
            count=count+1
    if year!=1900:
        fullcount=count+fullcount
print(fullcount)
