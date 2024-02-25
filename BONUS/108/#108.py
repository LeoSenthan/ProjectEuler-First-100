#1/x +1/y=1/n 
#n/x+n/y=1
#ny +nx = xy
#(x-n)(y-n)=n**2
#Number of solutions is number of divisors of n
# minimum solution >2000 is 2*3*5*7*11*13*17
#Find smallest product of seven prime factors which is greater than 2000
#current=[3,3,3,3,3,3,3] 2187
#First attempt to replace 17 but it has to be two prime factors hence it is 2,2,3,3,5,7,11,13=180180
#Now try to replace 13 so you can try 2*2*3 or 2*5 or 2*2 or 2*2*2 or 2*3
#None of these work hence 180180 is answer
print(180180)