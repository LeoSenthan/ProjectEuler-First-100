with open("089/#089.txt") as f:
    numbers=f.read().split("\n")
#I=1,V=5,X=10,L=50,C=100,D=500,M=1000
def Converted(roman):
    result = roman
    replacements = [
        ("VIIII", "IX"), 
        ("IIII", "IV"), 
        ("LXXXX", "XC"), 
        ("XXXX", "XL"),
        ("DCCCC", "CM"), 
        ("CCCC", "CD"),
    ]
    for old, improvement in replacements:
        result = result.replace(old, improvement)
    return result
original=0
improved=0
for number in numbers:
    original += len(number)
    improved += len(Converted(number))
print(original - improved)