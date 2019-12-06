def get_by_mode(value, position, mode):
    if mode:
        return value
    return position


def compute(original_data, input):
    # copy of data
    data = [x for x in original_data]

    last_output = 0

    pointer = 0
    while(pointer < len(data)):
        A = data[pointer] // 10000 % 10
        B = data[pointer] // 1000 % 10
        C = data[pointer] // 100 % 10
        opcode = data[pointer] % 100
        if opcode != 3 or opcode != 4:
            if C:
                param1 = data[pointer+1]
            else:
                param1 = data[data[pointer+1]]
            if B:
                param2 = data[pointer+2]
            else:
                param2 = data[data[pointer+2]]

        if opcode == 1:
            if A:
                data[pointer+3] = param1 + param2
            else:
                data[data[pointer+3]] = param1 + param2
            pointer += 4
        elif opcode == 2:
            if A:
                data[pointer+3] = param1 * param2
            else:
                data[data[pointer+3]] = param1 * param2
            pointer += 4
        elif opcode == 3:
            if C:
                data[pointer+1] = input
            else:
                print('WEIRD???')
                data[data[pointer+1]] = input
            pointer += 2
        elif opcode == 4:
            pointer += 2
            last_output = data[pointer+1]
        elif opcode == 5:
            if param1 != 0:
                pointer = data[pointer+2]
            else:
                pointer += 3
        elif opcode == 6:
            if param1 == 0:
                pointer = data[pointer+2]
            else:
                pointer += 3
        elif opcode == 7:
            print('OPCODE 7')
            print(data[pointer])
            if param1 < param2:
                data[data[pointer+3]] = 1
            else:
                data[data[pointer+3]] = 0
        elif opcode == 8:
            print('OPCODE 8')
            print(data[pointer])
            if param1 == param2:
                data[data[pointer+3]] = 1
            else:
                data[data[pointer+3]] = 0
        elif opcode == 99:
            print('HALTED WITH 99')
            return last_output
        else:
            raise ValueError('Wrong optocode, pointer: {0}, opcode {1}'.format(pointer, opcode))

    print('CODE DID NOT HALT. :(')
    return None


def main():
    data = open('input.txt', 'r').read().strip().split(',')
    data = [int(x) for x in data]

    input = 5

    output = compute(data, input)

    print("CODE IS: {0}".format(output))


if __name__ == "__main__":
    main()
