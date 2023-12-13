DEBUG = 1

N = [chunk.splitlines() for chunk in open(
    './in/13.test.txt').read().split('\n\n')]
N = [chunk.splitlines() for chunk in open('./in/13.txt').read().split('\n\n')]


def col(chunk, j):
    return [row[j] for row in chunk]


def part_1():
    # assuming no frame has both v and h reflection
    t = 0
    # checking for h is easier
    for _, chunk in enumerate(N):
        H = len(chunk)
        W = len(chunk[0])
        DEBUG and print('Chunk', _)
        for i in range(H - 1):
            if chunk[i] == chunk[i + 1]:
                DEBUG and print(
                    f'Rows {i} and {i + 1} match! starting a search...')

                for above, below in zip(range(i - 1, -1, -1), range(i + 2, H)):
                    if chunk[above] != chunk[below]:
                        DEBUG and print(
                            f'Not a match: rows {above} and {below}')
                        break
                else:
                    DEBUG and print('H-match!')
                    t += 100 * (i + 1)
                    break
        else:
            DEBUG and print('\nNo h-matches, now checking for v')
            for j in range(W - 1):
                if col(chunk, j) == col(chunk, j + 1):
                    DEBUG and print(
                        f"Cols {j} and {j + 1} match! starting a search...")
                    for left, right in zip(range(j - 1, -1, -1), range(j + 2, W)):
                        if col(chunk, left) != col(chunk, right):
                            DEBUG and print(
                                f'Not a match: cols {left} and {right}')
                            break
                    else:
                        DEBUG and print('V-match!')
                        t += j + 1
                        break
        DEBUG and print()
    return t


def part_2():
    pass


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(part_1())
    print('\n--- Part 2 ---')
    print(part_2())
