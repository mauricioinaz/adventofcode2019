from collections import defaultdict
from intcode_computer import compute

DIRECTIONS = {
    0: [0, 1],
    1: [1, 0],
    2: [0, -1],
    3: [-1, 0]
}


def main():
    data = open('input.txt', 'r').read().strip().split(',')
    data = [int(x) for x in data]
    data = data + [0]*1000

    loc = [100, 100]
    direction = 0
    grid = [['.' for _ in range(200)] for _ in range(200)]
    panels_painted = defaultdict()
    halted = False
    pointer = 0
    rel_base = 0
    while not halted:
        # Read panel and paint
        input = 0 if grid[loc[0]][loc[1]] == '.' else 1
        output, data, halted, pointer, rel_base = compute(data, input, pointer, rel_base)
        grid[loc[0]][loc[1]] = '#' if output else '.'
        panels_painted[tuple(loc)] = grid[loc[0]][loc[1]]
        # Rotare 90º left or right
        output, data, halted, pointer, rel_base = compute(data, input, pointer, rel_base)
        if output:
            direction += 1
        else:
            direction -= 1
        loc = [x + y for x, y in zip(loc, DIRECTIONS[direction % 4])]

    print(f'Number of painter panles is: {len(panels_painted.keys())}')


if __name__ == "__main__":
    main()
