
from collections import Counter


DEBUG = 0

if DEBUG:
    N = [line.strip() for line in open('./in/4.test.txt').readlines()]
else:
    N = [line.strip() for line in open('./in/4.txt').readlines()]

cards = []
for line in N:
    line = line[line.index(':') + 1:]
    scratched, winners = map(str.split, line.split(' | '))
    cards.append(tuple([
        set(int(x) for x in scratched),
        set(int(x) for x in winners)]
    ))

    assert len(scratched) == len(cards[-1][0])
    assert len(winners) == len(cards[-1][1])


def part_1():
    t = 0
    for scratched, winners in cards:
        if k := scratched & winners:
            t += 1 << (len(k) - 1)

    return t


def part_2():
    c = Counter()

    for i, (scratched, winners) in enumerate(cards):
        c[i] += 1

        k = len(scratched & winners)
        for j in range(k):
            c[i + j + 1] += c[i]

    return sum(c.values())


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(part_1())
    print('\n--- Part 2 ---')
    print(part_2())
