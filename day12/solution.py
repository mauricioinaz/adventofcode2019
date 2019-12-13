POS = 'position'
VEL = 'velocity'
IO = {
    POS: {'x': -13, 'y': -13, 'z': -13},
    VEL: {'x': 0, 'y': 0, 'z': 0}
}
EUROPA = {
    POS: {'x': 5, 'y': -8, 'z': 3},
    VEL: {'x': 0, 'y': 0, 'z': 0}
}
GANYMEDE = {
    POS: {'x': -6, 'y': -10, 'z': -3},
    VEL: {'x': 0, 'y': 0, 'z': 0}
}
CALLISTO = {
    POS: {'x': 0, 'y': 5, 'z': -5},
    VEL: {'x': 0, 'y': 0, 'z': 0}
}
JUPITER_MOONS = [IO, EUROPA, GANYMEDE, CALLISTO]
AXES = ['x', 'y', 'z']


def main():
    step = 0
    while step < 1000:
        # Apply Gravity
        for i, moon_a in enumerate(JUPITER_MOONS):
            for moon_b in JUPITER_MOONS[i+1:]:
                for axis in AXES:
                    if moon_a[POS][axis] > moon_b[POS][axis]:
                        moon_b[VEL][axis] += 1
                        moon_a[VEL][axis] -= 1
                    elif moon_a[POS][axis] < moon_b[POS][axis]:
                        moon_a[VEL][axis] += 1
                        moon_b[VEL][axis] -= 1
        # Apply Velocity
        for moon in JUPITER_MOONS:
            for axis in AXES:
                moon[POS][axis] += moon[VEL][axis]
        step += 1

    # Calculate energies
    total_energy = 0
    for moon in JUPITER_MOONS:
        energy = {POS: 0, VEL: 0}
        for x in moon:
            for value in moon[x].values():
                energy[x] += abs(value)
        total_energy += energy[POS]*energy[VEL]

    print(f'Total energy is: {total_energy}')


if __name__ == "__main__":
    main()
