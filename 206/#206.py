from math import sqrt
#2nd last digit is 0 since last digit is 0
square="1_2_3_4_5_6_7_8_900"
for n1 in range(0,10):
    for n2 in range(0,10):
        for n3 in range(0,10):
            for n4 in range(0,10):
                for n5 in range(0,10):
                    for n6 in range(0,10):
                        for n7 in range(0,10):
                            for n8 in range(0,10):
                                combo=int(square[0]+str(n1)+square[2]+str(n2)+square[4]+str(n3)+square[6]+str(n4)+square[8]+str(n5)+square[10]+str(n6)+square[12]+str(n7)+square[14]+str(n8))
                                if sqrt(combo)%1==0:
                                    print(combo,sqrt(combo)*10)
                                    break
                                                              