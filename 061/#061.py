polygonal_numbers = {
    "triangular": [(x//100, x%100) for x in [n*(n+1)//2 for n in range(45, 141)]],
    "square": [(x//100, x%100) for x in [n**2 for n in range(32, 100)]],
    "pentagonal": [(x//100, x%100) for x in [n*(3*n-1)//2 for n in range(26, 82)]],
    "hexagonal": [(x//100, x%100) for x in [n*(2*n-1) for n in range(23, 71)]],
    "heptagonal": [(x//100, x%100) for x in [n*(5*n-3)//2 for n in range(21, 64)]],
    "octagonal": [(x//100, x%100) for x in [n*(3*n-2) for n in range(19, 59)]]
}
#octagonal numbers are the starting point
for n1 in polygonal_numbers["octagonal"]:

    for polygon2 in polygonal_numbers.values():
        if polygon2 != polygonal_numbers["octagonal"]:
            for n2 in polygon2:
                if n1[1] == n2[0]:
                    # Iterate through remaining polygonal number types for subsequent numbers
                    for polygon3 in polygonal_numbers.values():
                        if polygon3 not in(polygon2, polygonal_numbers["octagonal"]):
                            for n3 in polygon3:
                                if n2[1] == n3[0]:

                                    for polygon4 in polygonal_numbers.values():
                                        if polygon4 not in (polygon3, polygon2, polygonal_numbers["octagonal"]):
                                            for n4 in polygon4:
                                                if n3[1] == n4[0]:

                                                    for polygon5 in polygonal_numbers.values():
                                                        if polygon5 not in (polygon4, polygon3, polygon2, polygonal_numbers["octagonal"]):
                                                            for n5 in polygon5:
                                                                if n4[1] == n5[0]:

                                                                    for polygon6 in polygonal_numbers.values():
                                                                        if polygon6 not in (polygon5, polygon4, polygon3, polygon2, polygonal_numbers["octagonal"]):
                                                                            for n6 in polygon6:
                                                                                if n6[0] == n5[1] and n6[1] == n1[0]:
                                                                                    chain = [n1, n2, n3, n4, n5, n6]
                                                                                    print(sum(num[0]*100+num[1] for num in chain))