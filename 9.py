DEBUG = 0

N = [line.strip() for line in open('./in/9.test.txt').readlines()]
N = [line.strip() for line in open('./in/9.txt').readlines()]

N = [list(map(int, line.split())) for line in N]


def nth_in_sequence(seq, n, sign='+', degree=0):
    if all(x == 0 for x in seq):
        return 0
    DEBUG and print(degree, seq)
    diffs = [b - a for a, b in zip(seq, seq[1:])]

    return seq[n] + \
        (1 if sign == '+' else -1) * nth_in_sequence(diffs, n, sign, degree + 1)


def part_1():
    return sum(nth_in_sequence(ln, -1) for ln in N)


def part_2():
    return sum(nth_in_sequence(ln, 0, '-') for ln in N)


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(part_1())
    print('\n--- Part 2 ---')
    print(part_2())
