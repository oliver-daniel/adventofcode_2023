
from collections import defaultdict
from math import prod


DEBUG = 0

if DEBUG:
    N = [line.strip() for line in open('./in/2.test.txt').readlines()]
else:
    N = [line.strip() for line in open('./in/2.txt').readlines()]

games = defaultdict(list)

for line in N:
    gid, tokens = line.split(': ')
    gid = int(gid.split(' ')[-1])

    for group in tokens.split('; '):
        shown = {}
        for amt, color in map(str.split, group.split(', ')):
            shown[color] = int(amt)
        games[gid].append(shown)


def part_1():
    seed = {
        'red': 12,
        'green': 13,
        'blue': 14
    }

    possible = []

    for gid, rounds in games.items():
        for rd in rounds:
            if any(seed[key] < rd.get(key, 0) for key in seed.keys()):
                if DEBUG:
                    print(f'game {gid} is impossible ({rd})')
                break
        else:
            possible.append(gid)
    return sum(possible)


def part_2():

    t = 0
    for rounds in games.values():
        required = {
            key: max(rd.get(key, 0) for rd in rounds)
            for key in ['red', 'green', 'blue']
        }

        t += prod(required.values())
    return t


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(part_1())
    print('\n--- Part 2 ---')
    print(part_2())
