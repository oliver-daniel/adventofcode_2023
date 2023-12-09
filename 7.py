from collections import Counter
from functools import cmp_to_key


DEBUG = 0

N = [line.strip() for line in open('./in/7.test.txt').readlines()]
N = [line.strip() for line in open('./in/7.txt').readlines()]

values = {
    k: i for i, k in enumerate('23456789TJQKA')
}

strength_lookup = {
    (5,): 6,
    (1, 4): 5,
    (2, 3): 4,
    (1, 1, 3): 3,
    (1, 2, 2): 2,
    (1, 1, 1, 2): 1,
    (1, 1, 1, 1, 1): 0
}


class Hand:
    def __init__(self, cards: str, bid: int):
        self._cards = cards
        self.bid = bid
        self.cards = [
            values[card] for card in cards
        ]
        self._counts = Counter(cards)

        counts = sorted(self._counts.values())
        self.hand_strength = strength_lookup[tuple(counts)]

    @property
    def p2(self):
        counts_cpy = self._counts.copy()

        jokers = counts_cpy['J']
        del counts_cpy['J']
        remaining = (sorted(counts_cpy.values()))

        for hand in strength_lookup:
            if len(hand) != len(remaining):
                continue

        if len(remaining) == 0:
            new_hand = (5,)
        else:
            new_hand = next(hand for hand in strength_lookup if len(hand) == len(remaining)
                            and all(remaining[i] <= hand[i] for i in range(len(hand)))
                            )

        return {
            'cards': [value if value != values['J'] else -1 for value in self.cards],
            'hand_strength': strength_lookup[new_hand]
        }

    def __repr__(self):
        return f'<{self._cards}, {self.hand_strength}, {self.bid}>'


hands = []

for cards, bid in map(str.split, N):
    hands.append(Hand(cards, int(bid)))


def part_1():
    def comp(self, other: Hand):
        if self.hand_strength != other.hand_strength:
            return self.hand_strength < other.hand_strength

        for this, that in zip(self.cards, other.cards):
            if this != that:
                return this < that
        return False

    Hand.__lt__ = comp

    ret = sorted(hands)
    t = 0
    for i, hand in enumerate(ret, start=1):
        t += i * hand.bid

    return t


def part_2():
    def comp(self, other: Hand):
        eff_self = self.p2
        eff_other = other.p2

        if eff_self['hand_strength'] != eff_other['hand_strength']:
            return eff_self['hand_strength'] < eff_other['hand_strength']
        
        for this, that in zip(eff_self['cards'], eff_other['cards']):
            if this != that:
                return this < that
        return False
    
    Hand.__lt__ = comp

    ret = sorted(hands)
    t = 0
    for i, hand in enumerate(ret, start=1):
        t += i * hand.bid

    return t


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(part_1())
    print('\n--- Part 2 ---')
    print(part_2())
