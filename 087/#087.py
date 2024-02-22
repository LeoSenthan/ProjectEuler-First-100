#Lowest is 28
#X=A**2+B**3+C**3
#Max C value is 7072 as root 50,000,000 is 7071
def SieveOfEratosthenes(num):
  list1=[]
  prime = [True for i in range(num+1)]
  p = 2
  while (p * p <= num):
      if (prime[p] == True):
          for i in range(p * p, num+1, p):
              prime[i] = False
      p += 1
  for p in range(2, num+1):
      if prime[p]:
          list1.append(p)
  return list1
list1=SieveOfEratosthenes(7072)
possible=[]
for C in list1:
    for B in list1:
        for A in list1:
            if A**2+B**3+C**4>50000000:
                break
            else:
                possible.append(A**2+B**3+C**4)
print(len(list(set(possible))))
