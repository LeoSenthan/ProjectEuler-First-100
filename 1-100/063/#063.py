#a^^b for no of digits to be correct a<10
power=0
count=0
while True:
    power+=1
    for a in range(1,10):
        if len(str(a**power))==power:
            count+=1
            print(count)
#Since it stops at 49 and then error occurs due to limit for integer string conversions
#Answer probably 49