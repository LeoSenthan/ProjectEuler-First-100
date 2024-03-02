n=0
while True:
    n+=1
    checker=sorted(str(n))
    if sorted(str(n*2))==checker:
        if sorted(str(n*3))==checker:
            if sorted(str(n*4))==checker:
                if sorted(str(n*5))==checker:
                    if sorted(str(n*6))==checker:
                        print(n)
                        exit()