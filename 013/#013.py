#013
import os

with open("013/#013.txt","r") as f:
    numbers=f.readlines()
total=0
for number in numbers:
    total=total+int(number[0:12])
print(str(total)[0:10])