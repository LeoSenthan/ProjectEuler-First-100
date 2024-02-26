from math import factorial
probabilities=[1,0,0,0,0,0,0,0]
for turn in range(0,16):
    for combos in range(7, 0, -1):
        probabilities[combos]+=turn*probabilities[combos-1]
#Odds of winning are (factorial(16) / sum(probabilities))
#Hence prize fund is 1/result which is the calculation flipped
print (factorial(16) / sum(probabilities))