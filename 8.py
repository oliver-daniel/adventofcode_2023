import itertools as it
from math import lcm
DEBUG = 0

# N = [line.strip() for line in open('./in/8.test.txt').readlines()]
# N = [line.strip() for line in open('./in/8.test.2.txt').readlines()]
# N = [line.strip() for line in open('./in/8.test.3.txt').readlines()]
N = [line.strip() for line in open('./in/8.txt').readlines()]


pattern, _, *lines = N

tree = {
    a: (b[1:-1], c[:-1]) for a, _, b, c in map(str.split, lines)
}

GOAL = 'ZZZ'


def part_1():
    START = 'AAA'
    curr = START
    for i, dirn in enumerate(it.cycle(pattern)):
        if curr == GOAL:
            return i
        curr = tree[curr][dirn == 'R']


def part_2():
    pointers = [node for node in tree if node.endswith('A')]
    start = pointers[:]

    offsets = [0 for _ in pointers]
    cycle_lengths = [0 for _ in pointers]

    # discovered invariant:
    # each pointer only cycles through
    # *one* node with a Z

    for i, dirn in enumerate(it.cycle(pattern)):
        for j, node in enumerate(pointers):
            if node.endswith('Z'):
                if offsets[j] == 0:
                    offsets[j] = i
                elif cycle_lengths[j] == 0:
                    cycle_lengths[j] = i - offsets[j]
        if all(cycle_lengths):
            break
        pointers = [tree[curr][dirn == 'R'] for curr in pointers]
        DEBUG and print(i, cycle_lengths)

    return lcm(*cycle_lengths)


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(part_1())
    print('\n--- Part 2 ---')
    print(part_2())
