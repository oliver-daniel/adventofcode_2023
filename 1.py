
TEST = 0

if TEST:
    # N = [line.strip() for line in open('./in/1.test.txt').readlines()]
    N = [line.strip() for line in open('./in/1.test.2.txt').readlines()]
else:
    N = [line.strip() for line in open('./in/1.txt').readlines()]


def part_1():
    return sum(
        10 * (digits := [int(c) for c in ln if c.isnumeric()])[0] + digits[-1] for ln in N
    )


def part_2():
    digits = [
        'one',
        'two',
        'three',
        'four',
        'five',
        'six',
        'seven',
        'eight',
        'nine',
    ]
    
    t = 0

    for ln in N:
        found = []
        for i, c in enumerate(ln):
            if c.isnumeric():
                found.append(int(c))
                continue
            
            for value, digit in enumerate(digits, start=1):
                if ln[i : i + len(digit)] == digit:
                    found.append(value)
        t += 10 * found[0] + found[-1]

    return t


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(part_1())
    print('\n--- Part 2 ---')
    print(part_2())
