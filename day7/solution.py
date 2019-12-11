def compute(data, input, last_output, pointer, phase_used):
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
                if not phase_used:
                    data[pointer+1] = input
                    phase_used = True
                else:
                    data[pointer+1] = last_output
            else:
                if not phase_used:
                    data[data[pointer+1]] = input
                    phase_used = True
                else:
                    data[data[pointer+1]] = last_output
            pointer += 2
        elif opcode == 4:
            if C:
                last_output = data[pointer+1]

            else:
                last_output = data[data[pointer+1]]
            pointer += 2
            return data, last_output, pointer, False, phase_used
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
            return data, last_output, pointer, True, phase_used
        else:
            raise ValueError('Wrong opcode, pointer: {0}, opcode {1}'.format(pointer, opcode))

    print('CODE DID NOT HALT. :(')
    return data, last_output


def amplifier_controller(phases, original_data):
    last_output = 0
    all_thruster_outputs = []
    halted = False
    phase_used = [False for _ in range(5)]
    data = [x for x in original_data]
    amp_states = [[x for x in data] for _ in range(5)]
    amp_pointers = [0, 0, 0, 0, 0]
    while not halted:
        for i, phase in enumerate(phases):
            amp_states[i], last_output, amp_pointers[i], halted, phase_used[i] = compute(amp_states[i], phase, last_output, amp_pointers[i], phase_used[i])
            if i == 4:
                all_thruster_outputs.append(last_output)
    return max(all_thruster_outputs)


def main():
    data = open('input.txt', 'r').read().strip().split(',')
    data = [int(x) for x in data]

    # TESTS
    # amplifier_controller([9, 7, 8, 5, 6], data)
    # amplifier_controller([9, 8, 7, 6, 5], data)

    # this should be done in a cleaner way! :(
    all_phases = []
    for a in range(5, 10):
        for b in range(5, 10):
            for c in range(5, 10):
                for d in range(5, 10):
                    for e in range(5, 10):
                        tmp = [a, b, c, d, e]
                        if len(tmp) == len(set(tmp)):
                            all_phases.append(tmp)

    biggest_thruster_signal = 0
    for phase_sequence in all_phases:
        last_signal = amplifier_controller(phase_sequence, data)
        if last_signal > biggest_thruster_signal:
            biggest_thruster_signal = last_signal

    print(biggest_thruster_signal)


if __name__ == "__main__":
    main()
