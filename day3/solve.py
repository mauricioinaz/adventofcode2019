from collections import defaultdict

COMPASS = {
    'U': (1, 0),
    'D': (-1, 0),
    'R': (0, 1),
    'L': (0, -1)
}


def calc_manhattan(tup):
    return abs(tup[0]) + abs(tup[1])


def main():
    input = list(open('input.txt', 'r'))

    # Separate cables
    input = [cable.strip().split(',') for cable in input]

    # Calculate routes and crossings
    cable_route = {}
    wire_crosses = set()
    for i, cable in enumerate(input):
        location = (0, 0)
        for corner in cable:
            direction = COMPASS[corner[0]]
            steps = int(corner[1:])
            while steps > 0:
                location = tuple(a+b for a, b in zip(direction, location))
                if i == 0:
                    cable_route[location] = location
                elif i == 1:
                    if cable_route.get(location):
                        wire_crosses.add(location)
                steps -= 1

    # Find Shortest distance
    shortes_distance = calc_manhattan(wire_crosses.pop())
    tmp = shortes_distance
    while wire_crosses:
        tmp = calc_manhattan(wire_crosses.pop())
        if tmp < shortes_distance:
            shortes_distance = tmp

    print(shortes_distance)


if __name__ == "__main__":
    main()
