def generate_fibonacci(n):
    fibonacci_sequence = [0, 1]  
    for i in range(2, n):
        fibonacci_sequence.append(fibonacci_sequence[i-1] + fibonacci_sequence[i-2])
    return fibonacci_sequence
fibonacci_numbers = generate_fibonacci(10)[2:]

def digitsum(digitsum):
    result=""
    while digitsum>0:
        if digitsum>=9:
            result+="9"
            digitsum-=9
        elif digitsum>0:
            result+=str(digitsum)
            digitsum=0
    return(int(result[::-1]))
#S(k)=6(10**q-1)-9q+r((r+3)*10**q-2)/2
#k=9q+r
#
#r=90
#i=2
#k=9q+r
for fibbonaci in fibonacci_numbers:
    S(fibbonaci)=6()
