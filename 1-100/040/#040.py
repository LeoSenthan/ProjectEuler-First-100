string=""
n=0
while len(string)<1000001:
    n+=1
    string+=str(n)
print(int(string[0])*int(string[9])*int(string[99])*int(string[999])*int(string[9999])*int(string[99999])*int(string[999999]))