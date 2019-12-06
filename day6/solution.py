class Space_Object:
    def __init__(self, input, is_com=False):
        if is_com:
            self.name = input
            self.orbits_around = None
        else:
            self.name = input[4:]
            self.orbits_around = input[:3]

    def jumps_to_com(self, all_objects):
        all_jumps = set()
        tmp_obj = self
        while tmp_obj.orbits_around:
            all_jumps.add(tmp_obj.name)
            tmp_obj = all_objects[tmp_obj.orbits_around]

        return all_jumps


def main():
    data = list(open('input.txt', 'r'))
    data = [d.strip() for d in data]

    celestial_objects = {'COM': Space_Object('COM', True)}

    for orbit in data:
        tmp_obj = Space_Object(orbit)
        celestial_objects[tmp_obj.name] = tmp_obj

    # PART 1
    # checksum = 0
    # for obj_name in celestial_objects:
    #     tmp_obj = celestial_objects[obj_name]
    #     while tmp_obj.orbits_around:
    #         checksum += 1
    #         tmp_obj = celestial_objects[tmp_obj.orbits_around]
    #
    # print(checksum)

    # PART 2
    you = celestial_objects['YOU']
    santa = celestial_objects['SAN']

    you_jumps = you.jumps_to_com(celestial_objects)
    santa_jumps = santa.jumps_to_com(celestial_objects)

    orbit_transfers = len(you_jumps - santa_jumps) + len(santa_jumps - you_jumps) - 2
    print('The minimum orbital transfers is: {}'.format(orbit_transfers))


if __name__ == "__main__":
    main()
