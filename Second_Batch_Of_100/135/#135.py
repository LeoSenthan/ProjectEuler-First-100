#(x+a)**2-x**2-(x-a)**2=nonlocal
#x(4*a-x)=n
#n=x*k
#4*a-x=kk a=(x+k)/4
from collections import Counter
def get_list(n):
    result = []
    for x in range(1, n + 1):
        limit = min(3 * x - 1, n // x)
        for k in range(1, limit + 1):
            if (x + k) % 4 == 0:
                result.append(x * k)
    return result
def list1(n):
    result = Counter(get_list(n))
    return [(key, value) for key, value in result.items()]

n = 1000000
result = list1(n)
solution = sum(1 for _, count in result if count == 10)
print(solution)
