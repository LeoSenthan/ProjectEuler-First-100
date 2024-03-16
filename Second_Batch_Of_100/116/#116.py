# number of ways with red recurrence relationship is nth term = n-1th term + n-2th term 
#starts with [1,2]
# number of ways with green recurrence relationship is nth term = n-1th term + n-3th term 
#starts with [1,2,2]
#number of ways with blue is n-1th n-4th
#starts with [1,2]
red=[1,2]
while len(red)<50:
    red.append(red[-1]+red[-2])
green=[1,1,2]
while len(green)<50:
    green.append(green[-1]+green[-3])
blue=[1,1,1,2]
while len(blue)<50:
    blue.append(blue[-1]+blue[-4])
print(green[49]+blue[49]+red[49]-3) # -3 are when it is only gray
