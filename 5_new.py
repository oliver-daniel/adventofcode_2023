from enum import Enum, auto
from functools import reduce

DEBUG = 1

N = open('./in/5.test.txt').read().split('\n\n')
# N = open('./in/5.txt').read().split('\n\n')


class Resource(Enum):
    SEED = auto()
    SOIL = auto()
    FERTILIZER = auto()
    WATER = auto()
    LIGHT = auto()
    TEMPERATURE = auto()
    HUMIDITY = auto()
    LOCATION = auto()


resources = list(Resource)

_seeds, *maps = N

ranges = {}

for src, dest, chunk in zip(resources, resources[1:], maps):
    _header, *lines = chunk.splitlines()
    if DEBUG:
        assert _header.upper() == f'{src.name}-TO-{dest.name} MAP:'
    ranges[src, dest] = []

    for line in lines:
        dest_start, src_start, length = map(int, line.split())
        delta = dest_start - src_start

        ranges[src, dest].append((range(src_start, src_start + length), delta))


def naive_range(src: Resource, dest: Resource, n: int):
    for rg, delta in ranges[src, dest]:
        if n in rg:
            return n + delta
    return n


def fold(n, convert=naive_range):
    return reduce(
        lambda acc, res: (res, convert(acc[0], res, acc[1])),
        resources[1:],
        (Resource.SEED, n))[1]


def part_1():
    seeds = list(map(int, _seeds.split()[1:]))
    return min(map(fold, seeds))


def part_2():
    pass


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(part_1())
    print('\n--- Part 2 ---')
    print(part_2())
