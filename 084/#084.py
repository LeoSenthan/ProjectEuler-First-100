import random

path = {i: 0 for i in range(0, 40)}
path[2] = path[17] = path[33] = "CC"
path[7] = path[22] = path[36] = "CH"
path[10], path[30] = "J", "G2J"
path[5] = path[15] = path[25] = path[35] = "R"
path[12] = path[28] = "U"
frequencies = [[i, 0] for i in range(0, 40)]
CC = [0, 10, "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A"]
CH = [0, 10, 11, 24, 39, 5, "R", "R", "U", "Sub3", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A"]

def Roll():
    a, b = random.randint(1, 4), random.randint(1, 4)
    return a + b,a,b

def handle_CH(current):
    odds = random.randint(0, 15)
    if isinstance(CH[odds], int):
        return CH[odds]
    elif CH[odds] == "Sub3":
        frequencies[current-3][1] += 1  
        return current - 3
    elif CH[odds] == "R":
        for check in range(current + 1, 39):
            if path[check] == "R":
                frequencies[check][1] += 1
                return check
        frequencies[5][1]+=1
        return 5
    elif CH[odds] == "U":
        for check in range(current + 1, 39):
            if path[check] == "U":
                frequencies[check][1] += 1
                return check
        return 11
    else:
        return current

current, rolls, previous_rolls = 0, 0, [[0, 1], [0, 1], [0, 0]]

while rolls < 1000000:
    total, a, b = Roll()  # Roll the dice
    current += total  # Move the current position
    rolls += 1
    current = current - 40 if current > 39 else current  # Handle board wrapping
    frequencies[current][1] += 1

    # Jail Check - Triple Doubles
    Flag = True
    for doubles in previous_rolls:
        if doubles[0] != doubles[1]:
            Flag = False
            break
    if Flag:
        if Flag or current == 10:  
            frequencies[10][1] += 1

    # Go To Jail Square
    if path[current] == "G2J":
        current = 10
        frequencies[10][1] += 1

    # Community Chest
    elif path[current] == "CC":
        odds = random.randint(0, 15)
        if CC[odds] == 0:
            current = 0
            frequencies[0][1] += 1
        elif CC[odds] == 10:
            frequencies[10][1] += 1

    # Chance
    elif path[current] == "CH":
        current = handle_CH(current)

    previous_rolls = [previous_rolls[1], previous_rolls[2], [a, b]]  # Update previous rolls

print(sorted(frequencies, key=lambda x: x[1], reverse=True))
#First two are 10 and 15 attempt the third digit in descending order of frequency as the difference is relatively small