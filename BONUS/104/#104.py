fibbonaci = [1, 1]
def top_digits(n):
    count=0
    while n:
        count += 1
        n//=10
    return n//(10**(count-9))
while True:
    x = fibbonaci[-1] + fibbonaci[-2]
    fibbonaci.append(x)
    backward = x % 10**9
    if set(str(backward)) == set("123456789"):
        forward=top_digits(x)
        if set(str(forward)) == set("123456789"):
            print(forward, backward)
            break
print(len(fibbonaci))
