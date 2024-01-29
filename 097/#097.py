#ending section is the difference combinations of 28433*x
start=28433
for i in range(0,7830457):
    start=start*2
    if len(str(start))>=10:
        start=int(str(start)[-10:])
print(int(start)+1)