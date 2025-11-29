#sum of correct perimeters sequence is [4,6,22,72,268,990,3694] using brute force
#plus +1 sequence is [16,196,2704]
#minus -1 sequence is [50,722,10082]
#side sequence is [5,65,901]
#other side sequence is [17,241,3361] 
# hence patter for first sequence is 901=65*14-5-4
# other pattern is 3361=241*14-17+4
list2,list1=[17,241,3361],[5,65,901]
realperimeters=[16,50,196,722,2704,10082]
while list1[-1]*3+1<1000000000:
    list1.append(list1[-1]*14-list1[-2]-4)
    realperimeters.append(list1[-1]*3+1)
    if realperimeters[-1]>1000000000:
        realperimeters=realperimeters[:-1]
while list2[-1]*3+1<1000000000:
    list2.append(list2[-1]*14-list2[-2]+4)
    realperimeters.append(list2[-1]*3-1)
    if realperimeters[-1]>1000000000:
        realperimeters=realperimeters[:-1]
print(sum(realperimeters))