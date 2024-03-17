multiplier=1504170715041707
dividor=4503599627370517
total = multiplier
while multiplier!=0:
    dividor %= multiplier
    while multiplier>=dividor:
        multiplier -= dividor
        total += multiplier
print(total)