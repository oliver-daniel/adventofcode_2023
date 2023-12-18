from collections import namedtuple
from dataclasses import dataclass
from enum import Enum
from typing import List
# from .17 import Dirn


DEBUG = 1

# N = [line.strip() for line in open('./in/18.test.txt').readlines()]
N = [line.strip() for line in open('./in/18.txt').readlines()]


class Dirn(Enum):
    UP = (-1, 0)
    DOWN = (+1, 0)
    LEFT = (0, -1)
    RIGHT = (0, +1)

    def __repr__(self):
        return self.name


LOOKUP = {
    'U': Dirn.UP,
    'D': Dirn.DOWN,
    'L': Dirn.LEFT,
    'R': Dirn.RIGHT
}


@dataclass
class Step:
    dirn: Dirn
    distance: int
    rgb: str


steps: List[Step] = []


for dirn, distance, rgb in map(str.split, N):
    steps.append(Step(
        LOOKUP[dirn],
        int(distance),
        rgb[1:-1]
    ))


def pp(visited: set):
    pts = {(v[0], v[1]) for v in visited}
    max_y = max(v[0] for v in pts)
    max_x = max(v[1] for v in pts)

    for i in range(max_y + 1):
        print("".join('.#'[(i, j) in pts] for j in range(max_x + 1)))


def part_1():
    curr = (0, 0, None)
    visited = {curr}

    for step in steps:
        dy, dx = step.dirn.value

        for _ in range(step.distance):
            i, j, _rgb = curr
            curr = (i + dy, j + dx, step.rgb)

            if DEBUG and curr in visited:
                print(f'Already seen {curr}')
                assert curr == (0, 0)

            visited.add(curr)

    # don't worry about rgbs yet
    pts = {(v[0], v[1]) for v in visited}

    curr = (1, 1)
    stack = [curr]

    while stack:
        curr = stack.pop()
        pts.add(curr)

        i, j = curr
        for dirn in Dirn:
            dy, dx = dirn.value

            if (ii := i + dy, jj := j + dx) not in pts:
                stack.append((ii, jj))
    return len(pts)


def part_2():
    # God damnit
    pass


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(part_1())
    print('\n--- Part 2 ---')
    print(part_2())
