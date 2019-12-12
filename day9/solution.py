def compute(data, input):
    relative_base = 0
    pointer = 0
    while(pointer < len(data)):
        # 0 position mode
        # 1 immediate mode
        A = data[pointer] // 10000 % 10
        B = data[pointer] // 1000 % 10
        C = data[pointer] // 100 % 10
        opcode = data[pointer] % 100
        if opcode != 99:
            if C == 0:
                p1_pointer = data[pointer+1]
            elif C == 1:
                p1_pointer = pointer+1
            elif C == 2:
                p1_pointer = data[pointer+1] + relative_base
            if not (opcode == 3 or opcode == 4 or opcode == 9):
                if B == 0:
                    p2_pointer = data[pointer+2]
                elif B == 1:
                    p2_pointer = pointer+2
                elif B == 2:
                    p2_pointer = data[pointer+2] + relative_base
                if not (opcode == 5 or opcode == 6):
                    if A == 0:
                        p3_pointer = data[pointer+3]
                    elif A == 1:
                        p3_pointer = pointer+3
                    elif A == 2:
                        p3_pointer = data[pointer+3] + relative_base
        if opcode == 1:
            data[p3_pointer] = data[p1_pointer] + data[p2_pointer]
            pointer += 4
        elif opcode == 2:
            data[p3_pointer] = data[p1_pointer] * data[p2_pointer]
            pointer += 4
        elif opcode == 3:
            data[p1_pointer] = input
            pointer += 2
        elif opcode == 4:
            last_output = data[p1_pointer]
            pointer += 2
            print(last_output)
            # return data, last_output, pointer, False
        elif opcode == 5:
            if data[p1_pointer] != 0:
                pointer = data[p2_pointer]
            else:
                pointer += 3
        elif opcode == 6:
            if data[p1_pointer] == 0:
                pointer = data[p2_pointer]
            else:
                pointer += 3
        elif opcode == 7:
            if data[p1_pointer] < data[p2_pointer]:
                data[p3_pointer] = 1
            else:
                data[p3_pointer] = 0
            pointer += 4
        elif opcode == 8:
            if data[p1_pointer] == data[p2_pointer]:
                data[p3_pointer] = 1
            else:
                data[p3_pointer] = 0
            pointer += 4
        elif opcode == 9:
            relative_base += data[p1_pointer]
            # print(f'rel base {relative_base}')
            pointer += 2
        elif opcode == 99:
            return last_output, data
        else:
            raise ValueError('Wrong opcode, pointer: {0}, opcode {1}'.format(pointer, opcode))

    print('CODE DID NOT HALT. :(')
    return last_output


def main():
    data = open('input.txt', 'r').read().strip().split(',')
    data = [int(x) for x in data]

    data = data + [0]*1000
    result, data = compute(data, 2)
    print(f'result is: {result}')


if __name__ == "__main__":
    main()
