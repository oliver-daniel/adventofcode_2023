#!/usr/bin/python3
from sys import argv

day = argv[1]

template = f"""
TEST = 1

if TEST:
    N = [line.strip() for line in open('./in/{day}.test.txt').readlines()]
else:
    N = [line.strip() for line in open('./in/{day}.txt').readlines()]

def part_1():
    pass

def part_2():
    pass

if __name__ == '__main__':
    print('--- Part 1 ---')
    print(part_1())
    print('\\n--- Part 2 ---')
    print(part_2())

"""

def buffer_in():
    buffer = []
    while True:
        try:
            line = input()
            buffer.append(line)
        except EOFError: break
    return "\n".join(buffer)

if __name__ == "__main__":
    print(f"Enter test data for day {day}, then CTRL+D:")
    with open(f'./in/{day}.test.txt', 'w+') as f:
        f.write(buffer_in())

    print(f"Enter real data, then CTRL+D:")
    with open(f'./in/{day}.txt', 'w+') as f:
        f.writelines(buffer_in())

    with open(f'./{day}.py', 'w+') as f:
        f.write(template)