#((n-1)**x+(n+1)**x)%n**2
#Values of x  which are even result in r=2
#Odd values result in 2*a*n
#Maximized at a**2-a as a =7 hence 7**2-7=42
#Even values maximized at n**2-2n
total=0
for n in range(3,1001):
    if n%2==0:
        total+=(n**2-(2*n))
    else:
        total+=(n**2-n)
print(total)