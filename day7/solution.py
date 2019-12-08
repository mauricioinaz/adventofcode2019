# Same ugly code as day 5 but using input as a list
def compute(original_data, input):
    # copy of data
    data = [x for x in original_data]

    last_output = 0

    pointer = 0
    while(pointer < len(data)):
        # 0 position mode
        # 1 immediate mode
        A = data[pointer] // 10000 % 10
        B = data[pointer] // 1000 % 10
        C = data[pointer] // 100 % 10
        opcode = data[pointer] % 100
        if not (opcode == 3 or opcode == 4 or opcode == 99):
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
                data[pointer+1] = input.pop()
            else:
                data[data[pointer+1]] = input.pop()
            pointer += 2
        elif opcode == 4:
            last_output = data[data[pointer+1]]
            pointer += 2
        elif opcode == 5:
            if param1 != 0:
                pointer = param2
            else:
                pointer += 3
        elif opcode == 6:
            if param1 == 0:
                pointer = param2
            else:
                pointer += 3
        elif opcode == 7:
            if param1 < param2:
                data[data[pointer+3]] = 1
            else:
                data[data[pointer+3]] = 0
            pointer += 4
        elif opcode == 8:
            if param1 == param2:
                data[data[pointer+3]] = 1
            else:
                data[data[pointer+3]] = 0
            pointer += 4
        elif opcode == 99:
            return data, last_output
        else:
            raise ValueError('Wrong opcode, pointer: {0}, opcode {1}'.format(pointer, opcode))

    print('CODE DID NOT HALT. :(')
    return data, last_output


def main():
    data = open('input.txt', 'r').read().strip().split(',')
    data = [int(x) for x in data]

    # this should be done in a cleaner way! :(
    all_phases = []
    for a in range(0, 5):
        for b in range(0, 5):
            for c in range(0, 5):
                for d in range(0, 5):
                    for e in range(0, 5):
                        tmp = [a, b, c, d, e]
                        if len(tmp) == len(set(tmp)):
                            all_phases.append(tmp)

    biggest_thruster_signal = 0
    for phase_sequence in all_phases:
        last_output = 0
        for input_instruction in phase_sequence:
            input_instr_seq = [last_output, input_instruction]
            _, last_output = compute(data, input_instr_seq)
        if last_output > biggest_thruster_signal:
            biggest_thruster_signal = last_output

    print(biggest_thruster_signal)


if __name__ == "__main__":
    main()