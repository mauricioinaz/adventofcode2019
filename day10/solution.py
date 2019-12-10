from math import atan2


def get_all_angles(x, y, data):
    all_angles = set()
    for i, row in enumerate(data):
        for j, column in enumerate(row):
            if column == '#':
                all_angles.add(atan2(x-j, y-i))
    return len(all_angles)


def main():
    data = list(open('input.txt', 'r'))
    data = [[c for c in row.strip()] for row in data]

    asteroids_viewed = {}
    for i, row in enumerate(data):
        for j, column in enumerate(row):
            if column == '#':
                asteroids_viewed[get_all_angles(j, i, data)] = (j, i)

    max_asteroids = max(asteroids_viewed.keys())
    # x, y result is inverted from problem
    print(f'Most asteroids viewed was {max_asteroids} at {asteroids_viewed[max_asteroids]}')


if __name__ == "__main__":
    main()
