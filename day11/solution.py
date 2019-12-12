# from collections import defaultdict
import matplotlib.pyplot as plt
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

    loc = [50, 50]
    direction = 3
    grid = [['.' for _ in range(100)] for _ in range(100)]
    grid[loc[0]][loc[1]] = '#'  # Start at white panel
    # panels_painted = defaultdict()
    halted = False
    pointer = 0
    rel_base = 0
    while not halted:
        # Read panel and paint
        input = 0 if grid[loc[0]][loc[1]] == '.' else 1
        output, data, halted, pointer, rel_base = compute(data, input, pointer, rel_base)
        grid[loc[0]][loc[1]] = '#' if output else '.'
        # panels_painted[tuple(loc)] = grid[loc[0]][loc[1]]

        # Rotare 90º left or right
        output, data, halted, pointer, rel_base = compute(data, input, pointer, rel_base)
        if output:
            direction += 1
        else:
            direction -= 1
        loc = [x + y for x, y in zip(loc, DIRECTIONS[direction % 4])]

    # PART 1
    # print(f'Number of painted panles is: {len(panels_painted.keys())}')

    # PART 2
    for i, row in enumerate(grid):
        for j, column in enumerate(row):
            grid[i][j] = 0 if grid[i][j] == '.' else 2
    plt.imshow(grid)
    plt.show()


if __name__ == "__main__":
    main()
