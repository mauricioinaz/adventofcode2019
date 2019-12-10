from math import atan2, sqrt
from collections import defaultdict


def get_all_in_view(x, y, data, get_all_data=False):
    all_angles = defaultdict(list)
    for i, row in enumerate(data):
        for j, column in enumerate(row):
            if column == '#':
                all_angles[atan2(x-j, y-i)].append((j, i,))
    if get_all_data:
        return all_angles
    return len(all_angles.keys())


def main():
    data = list(open('input.txt', 'r'))
    data = [[c for c in row.strip()] for row in data]

    ast_viewed = {}
    for i, row in enumerate(data):
        for j, column in enumerate(row):
            if column == '#':
                ast_viewed[get_all_in_view(j, i, data)] = (j, i)

    # PART 1
    max_ast = max(ast_viewed.keys())
    print(f'Most asteroids viewed was {max_ast} at {ast_viewed[max_ast]}')

    # PART 2
    mon_station_x = ast_viewed[max_ast][0]
    mon_station_y = ast_viewed[max_ast][1]
    asteroids_to_laser = get_all_in_view(mon_station_x, mon_station_y, data, True)

    # Order asteroids in each angle by closest to monitoring station
    for angle, ast_list in asteroids_to_laser.items():
        ordered_asteroids = {}
        for ast in ast_list:
            distance = sqrt((mon_station_x - ast[0])**2 + (mon_station_y - ast[1])**2)
            ordered_asteroids[distance] = ast
        asteroids_to_laser[angle] = ordered_asteroids

    # Shooting lasers at asteroids!
    ordered_angles = sorted(asteroids_to_laser.keys())
    angle_index = ordered_angles.index(0.0)
    nth = 1
    while nth < 201:
        asteroids_in_angle = asteroids_to_laser[ordered_angles[angle_index]]
        if asteroids_in_angle:
            closest_distance = min(asteroids_in_angle.keys())
            last_asteroid_shot = asteroids_in_angle[closest_distance]
            # print(f'{nth}th is at {last_asteroid_shot}')
            del asteroids_in_angle[closest_distance]
            nth += 1
        if angle_index == 0:
            angle_index = len(ordered_angles)-1
            print('360 loop')
        else:
            angle_index -= 1  # adjusting for inverted coordinate system

    print(f'200th asteroid was at {last_asteroid_shot}')
    print(f'{last_asteroid_shot[0]*100+last_asteroid_shot[1]}')


if __name__ == "__main__":
    main()
