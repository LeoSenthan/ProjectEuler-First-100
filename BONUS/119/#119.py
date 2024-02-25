#a2 =8**3 a10=614656=28**4
answers=[]
for base in range(2,100):
    for power in range(2,10):
        result = base ** power
        total=sum(int(i) for i in str(result))
        if total==base: 
            answers.append(result)
            if len(answers)==30:
                break
print(sorted(answers)[29])
