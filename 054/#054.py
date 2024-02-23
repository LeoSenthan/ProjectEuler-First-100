from itertools import *

S = []

def s_func(f):
    S.append(f)
    return f

def g(cards, length):
    return [k for k, g in groupby(sorted(v for v, s in cards)) if len(list(g)) == length]

def p(cards):
    a, b = tee(sorted(v for v, s in cards))
    next(b, None)
    return zip(a, b)

def suits(cards):
    return list({s for v, s in cards})

def c(hand):
    f = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    return sorted(((int(f.get(c[0], c[0])), c[1]) for c in hand), key=lambda x: x[0])

def parse_hands(lines):
    return ((c(l.split()[:5]), c(l.split()[5:])) for l in lines)

def winner(hands):
    return int(score(hands[0]) < score(hands[1])) + 1

def score(cards):
    highest_card = max(v for v, s in cards)
    pairs = g(cards, 2)
    one_pair = 1e2 + 2e1 * max(pairs) if len(pairs) == 1 else 0
    two_pair = 1e3 + 2e2 * max(pairs) if len(pairs) == 2 else 0
    threes = g(cards, 3)
    three_of_a_kind = 1e4 + 2e3 * max(threes) if len(threes) == 1 else 0
    is_straight = 1e5 * int(all(b - a == 1 for a, b in p(cards)))
    is_flush = 1e6 * int(len(suits(cards)) == 1)
    full_house = 1e7 * int(len(g(cards, 2)) == 1 and len(g(cards, 3)) == 1)
    fours = g(cards, 4)
    four_of_a_kind = 1e8 + 2e7 * max(fours) if len(fours) == 1 else 0
    is_straight_flush = 1e9 * int(len(suits(cards)) == 1 and all(b - a == 1 for a, b in p(cards)))
    is_royal_flush = 1e10 * int(len(suits(cards)) == 1 and [v for v, s in cards] == [10, 11, 12, 13, 14])
    return sum([highest_card, one_pair, two_pair, three_of_a_kind, is_straight, is_flush, full_house, four_of_a_kind, is_straight_flush, is_royal_flush])

with open('054/#054.txt', "r") as f:
    print(sum(1 for hands in parse_hands(f) if winner(hands) == 1))