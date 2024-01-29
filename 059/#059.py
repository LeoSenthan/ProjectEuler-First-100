#Key is three lower case characters possibilities is 26**3 which is 17576 
#Values of AaEeNnTt are 69,101,65,97,78,110,84,116,65,65
from operator import xor
max,truekey=0,[0,0,0]
with open("059/#059.txt") as f:
    ciphertext=f.read().split(",")
for key1 in range(97,122):
    for key2 in (97,122):
        for key3 in (97,122):
            commonletter=0
            for char in range(0,len(ciphertext)):
                if char%3==0:
                    current=key1
                elif char%3==1:
                    current=key2
                else:
                    current=key3
                if int(ciphertext[char]) ^ current in [69,101,65,97,78,110,84,116,65,65]:
                    commonletter+=1
            if commonletter>max:
                max,truekey=commonletter,[key1,key2,key3]
print(truekey)
for keyletter in truekey:
    print(chr(keyletter))
