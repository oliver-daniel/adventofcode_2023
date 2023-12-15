from collections import defaultdict


DEBUG = 1

N = open('./in/15.test.txt').readline().strip().split(',')
N = open('./in/15.txt').readline().strip().split(',')


def _hash(str):
    t = 0
    for char in str:
        t += ord(char)
        t *= 17
        t %= 256
    return t


def part_1():
    return sum(map(_hash, N))


def part_2():
    # Thanks, python 3.7+!
    boxes = defaultdict(dict)
    for step in N:
        if step[-2] == '=':
            label = step[:-2]
            box = _hash(label)
            focal_length = int(step[-1])
            boxes[box][label] = focal_length
        else:
            label = step[:-1]
            box = _hash(label)
            # assert step[-1] == '-'
            if label not in boxes[box]:
                continue
            del boxes[box][label]

    t = 0
    for box_n, contents in boxes.items():
        for i, focal_length in enumerate(contents.values(), start=1):
            t += (1 + box_n) * i * focal_length

    return t


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(part_1())
    print('\n--- Part 2 ---')
    print(part_2())
