COMPASS = {
    'U': (1, 0),
    'D': (-1, 0),
    'R': (0, 1),
    'L': (0, -1)
}


def main():
    input = list(open('input.txt', 'r'))

    # Separate cables
    input = [cable.strip().split(',') for cable in input]

    # Calculate routes and crossings
    cable_route = {}
    wire_crosses = []
    for i, cable in enumerate(input):
        location = (0, 0)
        total_steps = 0
        for corner in cable:
            direction = COMPASS[corner[0]]
            steps = int(corner[1:])
            while steps > 0:
                total_steps += 1
                location = tuple(a+b for a, b in zip(direction, location))
                # create first cable route
                if i == 0:
                    cable_route[location] = total_steps
                # find crossings with second cable
                elif i == 1:
                    if cable_route.get(location):
                        wire_crosses.append(total_steps + cable_route[location])
                steps -= 1

    print("Shortest distance is {} steps".format(min(wire_crosses)))


if __name__ == "__main__":
    main()
