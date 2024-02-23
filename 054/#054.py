from itertools import *
SCORE = []

def score_func(func):
    SCORE.append(func)
    return func
def groups(cards, length):
    return [k for k, g in groupby(sorted(value for value, suit in cards)) if len(list(g)) == length]
def pairwise(cards):
    a, b = tee(sorted(value for value, suit in cards))
    next(b, None)
    return zip(a, b)
def suits(cards):
    return list({suit for value, suit in cards})
def cards(hand):
    faces = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    return sorted(((int(faces.get(card[0], card[0])), card[1]) for card in hand), key=lambda x: x[0])
def parse_hands(lines):
    return ((cards(line.split()[:5]), cards(line.split()[5:])) for line in lines)
def winner(hands):
    return int(score(hands[0]) < score(hands[1])) + 1
def score(cards):
    highest_card = max(value for value, suit in cards)
    pairs = groups(cards, 2)
    one_pair = 1e2 + 2e1 * max(pairs) if len(pairs) == 1 else 0
    two_pair = 1e3 + 2e2 * max(pairs) if len(pairs) == 2 else 0
    threes = groups(cards, 3)
    three_of_a_kind = 1e4 + 2e3 * max(threes) if len(threes) == 1 else 0
    is_straight = 1e5 * int(all(b - a == 1 for a, b in pairwise(cards)))
    is_flush = 1e6 * int(len(suits(cards)) == 1)
    full_house = 1e7 * int(len(groups(cards, 2)) == 1 and len(groups(cards, 3)) == 1)
    fours = groups(cards, 4)
    four_of_a_kind = 1e8 + 2e7 * max(fours) if len(fours) == 1 else 0
    is_straight_flush = 1e9 * int(len(suits(cards)) == 1 and all(b - a == 1 for a, b in pairwise(cards)))
    is_royal_flush = 1e10 * int(len(suits(cards)) == 1 and [value for value, suit in cards] == [10, 11, 12, 13, 14])
    return sum([highest_card, one_pair, two_pair, three_of_a_kind, is_straight, is_flush, full_house, four_of_a_kind, is_straight_flush, is_royal_flush])

with open('054/#054.txt', "r") as f:
    print(sum(1 for hands in parse_hands(f) if winner(hands) == 1))