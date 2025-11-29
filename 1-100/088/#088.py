#Must be composite
#Minimal product-sum of k elements is k[lt]M<=2k
#Hence all solutions k[lt]M<=24000
def prodsum(product, sum, factors, start):
    k = product - sum + factors    # product - sum + number of factors
    if k < kmax:
        if product < n[k]: n[k] = product
        for i in range(start, kmax//product*2 + 1):
            prodsum(product*i, sum+i, factors+1, i) # Recursion
kmax=12001
n = [2*kmax] * kmax
prodsum(1, 1, 1, 2)
print (sum(set(n[2:])))