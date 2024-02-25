from math import sqrt
square = "1_2_3_4_5_6_7_8_9"
# Calculate the lower and upper bounds for x
lower_bound = int(sqrt(int(square.replace('_', '0'))))  # Replace '_' with '0' for lower bound
upper_bound = int(sqrt(int(square.replace('_', '9'))))  # Replace '_' with '9' for upper bound
#Since root ends in 9 it has to be a odd root
for x in range(lower_bound, upper_bound + 1,2):
    squarex = x**2
    match=True
    for i in range(len(square)):
        if square[i] != '_' and int(square[i]) != (squarex // 10**(len(square) - 1 - i)) % 10:
            match = False
            break
    if match:
        print(squarex*10)
        print(x)
        break
