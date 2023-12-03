from functools import cache
import itertools as it
DEBUG = 0

# N = [line.strip() for line in open('./in/3.test.txt').readlines()]
N = [line.strip() for line in open('./in/3.txt').readlines()]

H = len(N)
W = len(N[0])


@cache
def create_coords():
    symbol_coords = []
    number_coords = []

    for i in range(H):
        seek = 0
        while seek < W:
            c = N[i][seek]
            if c.isnumeric():
                digits = [c]
                lookahead = 1
                while seek + lookahead < W:
                    if not (peek := N[i][seek + lookahead]).isnumeric():
                        break
                    digits.append(peek)
                    lookahead += 1
                k = int("".join(digits))

                coords = []

                for j in range(lookahead):
                    coords.append((i, seek + j))

                number_coords.append((tuple(coords), k))

                seek += lookahead - 1

            elif c != '.':
                symbol_coords.append(((i, seek), c))

            seek += 1

    return symbol_coords, number_coords


@cache
def is_adjacent(number, symbol):
    coords, _sym = symbol

    for y, x in number[0]:
        dy = abs(coords[0] - y)
        dx = abs(coords[1] - x)
        if dy <= 1 and dx <= 1:
            return True
    return False


def part_1():
    symbol_coords, number_coords = create_coords()

    t = 0

    for number, symbol in it.product(number_coords, symbol_coords):
        if is_adjacent(number, symbol):
            DEBUG and print(
                f'{number[1]} is a valid part id (adjacent to {symbol[0]})'
            )
            t += number[1]
    return t


def part_2():
    symbol_coords, number_coords = create_coords()

    t = 0

    for symbol in symbol_coords:
        _coords, sym = symbol
        if sym != "*":
            continue

        adjacent = [
            number for number in number_coords if is_adjacent(number, symbol)]
        if len(adjacent) == 2:
            t += adjacent[0][1] * adjacent[1][1]
    return t


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(part_1())
    print('\n--- Part 2 ---')
    print(part_2())
