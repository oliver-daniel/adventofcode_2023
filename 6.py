DEBUG = 1

N = [line.strip() for line in open('./in/6.test.txt').readlines()]
N = [line.strip() for line in open('./in/6.txt').readlines()]

races = [
    (int(time), int(dist))
    for time, dist in zip(N[0].split()[1:], N[1].split()[1:])
]

def part_1():
    t = 1

    for time, dist in races:
        winning = [k for k in range(1, time) if k * (time - k) > dist]
        t *= len(winning)

    return t

def part_2():
    big_time = int("".join(str(time) for time, dist in races))
    big_dist = int("".join(str(dist) for time, dist in races))

    return len([k for k in range(1, big_time) if k * (big_time - k) > big_dist])

if __name__ == '__main__':
    print('--- Part 1 ---')
    print(part_1())
    print('\n--- Part 2 ---')
    print(part_2())

