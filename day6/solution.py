class Space_Object:
    def __init__(self, input, is_com=False):
        if is_com:
            self.name = input
            self.orbits_around = None
        else:
            self.name = input[4:]
            self.orbits_around = input[:3]


def main():
    data = list(open('input.txt', 'r'))
    data = [d.strip() for d in data]

    celestial_objects = {'COM': Space_Object('COM', True)}

    for orbit in data:
        tmp_obj = Space_Object(orbit)
        celestial_objects[tmp_obj.name] = tmp_obj

    checksum = 0
    for obj_name in celestial_objects:
        tmp_obj = celestial_objects[obj_name]
        while tmp_obj.orbits_around:
            checksum += 1
            tmp_obj = celestial_objects[tmp_obj.orbits_around]

    print(checksum)


if __name__ == "__main__":
    main()
