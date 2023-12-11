from collections import namedtuple
import itertools as it

TEST = 1
DEBUG = 1

N = [line.strip() for line in open(f'./in/10.test.{TEST}.txt').readlines()]
# N = [line.strip() for line in open('./in/10.txt').readlines()]

H = len(N)
W = len(N[0])

Pipe = namedtuple('Pipe', 'segment location neighbours')

pipes = {}
ANIMAL = (None, None)

NORTH = (-1, 0)
SOUTH = (+1, 0)
WEST = (0, -1)
EAST = (0, +1)

neighbour_deltas = {
    "|": (NORTH, SOUTH),
    '-': (EAST, WEST),
    'L': (NORTH, EAST),
    'J': (NORTH, WEST),
    '7': (SOUTH, WEST),
    'F': (SOUTH, EAST)
}

for i, j in it.product(range(H), range(W)):
    segment = N[i][j]
    if segment == '.':
        continue
    elif segment == 'S':
        ANIMAL = (i, j)
        continue

    ((di1, dj1), (di2, dj2)) = neighbour_deltas[segment]

    pipes[i, j] = Pipe(
        segment,
        (i, j),
        ((i + di1, j + dj1), (i + di2, j + dj2))
    )


def part_1():
    def advance(node: Pipe, G: dict, prev: tuple):
        k, w = node.neighbours
        _next = k if prev == w else w

        if _next not in G:
            DEBUG and print(f'{_next} is not a pipe')
            return None
        elif node.location not in G[_next].neighbours:
            DEBUG and print(
                node, 'and', G[_next], 'are not mutually neighbours', sep='\n')
            return None

        return _next

    i, j = ANIMAL
    # establish what kind of pipe S could be
    for segment, ((di1, dj1), (di2, dj2)) in neighbour_deltas.items():
        k = (i + di1, j + dj1)
        w = (i + di2, j + dj2)

        if k not in pipes or w not in pipes:
            continue
        elif ANIMAL not in pipes[k].neighbours or ANIMAL not in pipes[w].neighbours:
            continue

        DEBUG and print(f'Animal {ANIMAL} could be {segment}')

        hypothesis = {**pipes, ANIMAL: Pipe(segment, ANIMAL, (k, w))}

        curr1, curr2 = k, w
        prev1, prev2 = ANIMAL, ANIMAL

        seen1 = set()
        seen2 = set()

        for dist in it.count(2):
            next1 = advance(hypothesis[curr1], hypothesis, prev1)
            next2 = advance(hypothesis[curr2], hypothesis, prev2)

            if next1 is None or next2 is None:
                DEBUG and print('Not on the main track!', dist)
                break
            elif next1 not in hypothesis[curr1].neighbours or \
                    next2 not in hypothesis[curr2].neighbours:
                DEBUG and print('Not actually connected', dist)
                break
            elif next1 == next2:
                DEBUG and print(f'Met! {next1} {dist}')
                return dist
            elif next1 in seen1 or next2 in seen2:
                DEBUG and print('Not sure what to do here'. dist)
                break

            seen1.add(curr1)
            seen2.add(curr2)

            prev1, curr1 = curr1, next1
            prev2, curr2 = curr2, next2


def part_2():
    pass


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(part_1())
    print('\n--- Part 2 ---')
    print(part_2())
