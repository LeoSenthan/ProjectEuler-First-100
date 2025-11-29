from math import factorial
def choose(a,b):
    return(factorial(a)/(factorial(b)*factorial(a-b)))
def ways(n):
    n+=1
    total=0
    for k in range(0,int(n/(51)+1)):
        total+=choose(n-(49)*k,2*k)
    return total
#Rough Guessing
print(ways(167))
print(ways(168))