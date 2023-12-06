
from dataclasses import dataclass
from functools import cache
from typing import Dict, Literal, List, Tuple


DEBUG = 1

N = [line.strip() for line in open('./in/5.test.txt').readlines()]
# N = [line.strip() for line in open('./in/5.txt').readlines()]

_resources = ['seed', 'soil', 'fertilizer', 'water',
              'light', 'temperature', 'humidity', 'location']

Resource = Literal['seed', 'soil', 'fertilizer', 'water',
                   'light', 'temperature', 'humidity', 'location']


@dataclass
class Map:
    source: Resource
    dest: Resource
    mapping: List[Tuple[int, int, int]]

    def get(self, i: int) -> int:
        for src_start, dest_start, length in self.mapping:
            delta = i - src_start
            if 0 <= delta <= length:
                return dest_start + delta
        return i


_seeds, *_mappings = N
seeds = list(map(int, _seeds.split()[1:]))


@cache
def make_mappings():
    buffer = []
    ret: Dict[Tuple[Resource, Resource], Map] = {}

    for line in _mappings[1:] + ['']:
        if not line:
            description, *mappings = map(str.split, buffer)
            source, dest = description[0].split('-to-')

            ret[source, dest] = Map(source, dest, [])
            for dest_start, src_start, range_length in [map(int, row) for row in mappings]:
                DEBUG and print(
                    f'{source} ({src_start}..{src_start + range_length - 1}) -> {dest} ({dest_start}..{dest_start + range_length - 1})')
                ret[source, dest].mapping.append(
                    (src_start, dest_start, range_length))
                
                if dest_start < src_start:
                    print(f'...which is lower')

            buffer.clear()
            DEBUG and print()
            continue
        buffer.append(line)

    return ret


def part_1():
    mappings = make_mappings()

    def seed_to_location(i: int):
        curr = i
        for src, dest in zip(_resources, _resources[1:]):
            _curr = curr
            curr = mappings[src, dest].get(curr)
            DEBUG and print(f'{src} {_curr} -> {dest} {curr}')

        return curr

    return min(map(seed_to_location, seeds))


def part_2():
    mappings = make_mappings()

    def get_reverse(dest, src, i):
        mapping = mappings[src, dest]
        for src_start, dest_start, length in mapping.mapping:
            delta = i - dest_start
            if 0 <= delta <= length:
                return src_start + delta
        return i
    
    def location_to_seed(i):
        curr = i
        for dest, src in zip(_resources[::-1], _resources[-2::-1]):
            _curr = curr
            curr = get_reverse(dest, src, curr)
            DEBUG and print(f'{dest} {_curr} -> {src} {curr}')
        return curr

    expanded_seeds = [
        range(start, start + length) for start, length
        in zip(seeds[::2], seeds[1::2])
    ]

    location = 0
    while not any((test := location_to_seed(location)) in rg for rg in expanded_seeds):
        location += 1
        if location % 100 == 0: print(location)
        # print(f'{location} -> {test} not found')
    return location
if __name__ == '__main__':
    print('--- Part 1 ---')
    # print(part_1())
    print('\n--- Part 2 ---')
    print(part_2())
