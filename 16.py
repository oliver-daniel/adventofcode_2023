from dataclasses import dataclass
from enum import Enum
import itertools
from typing import Tuple


DEBUG = 0

# N = [line.strip() for line in open('./in/16.test.txt').readlines()]
N = [line.strip() for line in open('./in/16.txt').readlines()]

H = len(N)
W = len(N[0])


class Dirn(Enum):
    UP = (-1, 0)
    RIGHT = (0, 1)
    DOWN = (1, 0)
    LEFT = (0, -1)


@dataclass
class Beam:
    posn: Tuple[int, int]
    dirn: Dirn

    @property
    def active(self):
        i, j = self.posn
        return 0 <= i < H and 0 <= j < W


def part_1(seed_posn=(0, 0), seed_dirn=Dirn.RIGHT):
    beams = [Beam(seed_posn, seed_dirn)]

    def advance(beam: Beam):
        i, j = beam.posn

        tile = N[i][j]

        match tile, beam.dirn:
            case '|', (Dirn.LEFT | Dirn.RIGHT):
                DEBUG and print(f'| splitter hit at {beam.posn}, {beam.dirn}')
                beam.dirn = Dirn.UP
                beams.append(Beam(beam.posn, Dirn.DOWN))
            case '-', (Dirn.UP | Dirn.DOWN):
                DEBUG and print(f'- splitter hit at {beam.posn}, {beam.dirn}')
                beam.dirn = Dirn.LEFT
                beams.append(Beam(beam.posn, Dirn.RIGHT))
            case '/', Dirn.UP:
                beam.dirn = Dirn.RIGHT
            case '/', Dirn.DOWN:
                beam.dirn = Dirn.LEFT
            case '/', Dirn.RIGHT:
                beam.dirn = Dirn.UP
            case '/', Dirn.LEFT:
                beam.dirn = Dirn.DOWN
            case '\\', Dirn.UP:
                beam.dirn = Dirn.LEFT
            case '\\', Dirn.DOWN:
                beam.dirn = Dirn.RIGHT
            case '\\', Dirn.RIGHT:
                beam.dirn = Dirn.DOWN
            case '\\', Dirn.LEFT:
                beam.dirn = Dirn.UP

        dy, dx = beam.dirn.value

        ii, jj = i + dy, j + dx
        beam.posn = (ii, jj)

    visited = set()

    def pp():
        posns = {v[0] for v in visited}
        for i, j in itertools.product(range(H), range(W)):
            print('#' if (i, j) in posns else N[i][j], end='')
            if j == W - 1:
                print()

    while True:
        active = [beam for beam in beams if beam.active and (
            beam.posn, beam.dirn) not in visited]
        if len(active) == 0:
            break
        DEBUG and print(len(active), len(beams))

        for beam in active:
            visited.add((beam.posn, beam.dirn))
            advance(beam)
        DEBUG and pp()
        DEBUG and input()

    # don't double-count positions w different directions
    return len({v[0] for v in visited})


def part_2():
    best = 0

    for posns, dirn in [
        (((0, j) for j in range(W)), Dirn.DOWN),
        (((i, 0) for i in range(H)), Dirn.RIGHT),
        (((H - 1, j) for j in range(W)), Dirn.UP),
        (((i, W - 1) for i in range(H)), Dirn.LEFT),
    ]:
        best = max(best, max(part_1(posn, dirn) for posn in posns))

    return best


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(part_1())
    print('\n--- Part 2 ---')
    print(part_2())
