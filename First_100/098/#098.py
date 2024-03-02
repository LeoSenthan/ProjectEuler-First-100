with open("098/#098.txt") as f:
    words=f.read().split(",")
    for word in range(0,len(words)):
        words[word]=words[word].replace('"',"")
from collections import defaultdict

def find_anagram_pairs(words):
    anagram_groups = defaultdict(list)
    for word in words:
        if len(word) <= 4:
            continue
        sorted_word = ''.join(sorted(word))
        anagram_groups[sorted_word].append(word)
    anagram_pairs = [group for group in anagram_groups.values() if len(group) > 1]
    return anagram_pairs
anagram_pairs = find_anagram_pairs(words)
#Remove 3 letter words and 4 letter words  as they will most likely not have the highest square numbers
#Largest word is 9 letter pair INTRODUCE and REDUCTION

#Hence check possible square numbers between 1 and 999,999,999
#between 1 and 999,999,99  
squares=[]
for n in range(100,31622):
    counter=len(str(n**2))
    count=0
    Flag=True
    for char in "0123456789":
        if str(n**2).count(char)>1:
            Flag=False
    if Flag==True:
        squares.append(str(n**2))
from math import sqrt
for pair in anagram_pairs:
    print(pair)
    easy,hard="",""
    for n in range(0,len(pair[0])):
        easy+=str(n)
        hard+=str(pair[0].find(pair[1][n]))
    pair[0],pair[1]=easy,hard
    print(pair)
for pair in anagram_pairs:
    for square in squares:
        if len(str(square))==len(pair[0]):
            rearrangement=""
            for char in pair[1]:
                rearrangement+=str(square)[int(char)]
            if sqrt(int(rearrangement))%1==0:
                print(square,rearrangement)