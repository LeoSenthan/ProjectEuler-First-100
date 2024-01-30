with open("098/#098.txt") as f:
    words=f.read().split(",")
check=[]
for word in words:
    check.append(sorted(word.replace('"',"")))
