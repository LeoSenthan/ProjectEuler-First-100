addition_chains = [[[1]]]
total_length = 0
for num in range(2, 201):
    new_chains = []    
    for chain in addition_chains:
        for sub_chain in chain:
            for a in sub_chain:
                for b in sub_chain:
                    if a <= b and a + b == num:
                        new_chains.append(sub_chain + [num])    
    min_length = min(len(chain) for chain in new_chains)
    addition_chains.append([])
    for chain in new_chains:
        if len(chain) == min_length:
            addition_chains[-1].append(chain)
    total_length += min_length - 1
print(total_length)
