import itertools as it

DEBUG = 1

N = [line.strip() for line in open('./in/11.test.txt').readlines()]
N = [line.strip() for line in open('./in/11.txt').readlines()]

H = len(N)
W = len(N[0])

galaxies = [(i, j) for i, j in it.product(
    range(H), range(W)) if N[i][j] == '#']

rows_without = set(range(H)) - set([i for i, j in galaxies])
cols_without = set(range(W)) - set([j for i, j in galaxies])


def distance(a, b, expansion_factor=2):
    min_y = min(a[0], b[0])
    dy = abs(a[0] - b[0])
    min_x = min(a[1], b[1])
    dx = abs(a[1] - b[1])

    dist = 0
    for i in range(min_y, min_y + dy):
        dist += 1
        if i in rows_without:
            dist += expansion_factor - 1
    for j in range(min_x, min_x + dx):
        dist += 1
        if j in cols_without:
            dist += expansion_factor - 1

    return dist


def part_1():
    return sum(
        distance(a, b) for a, b in it.combinations(galaxies, r=2)
    )


def part_2():
    return sum(
        distance(a, b, 1_000_000) for a, b in it.combinations(galaxies, r=2)
    )


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(part_1())
    print('\n--- Part 2 ---')
    print(part_2())
