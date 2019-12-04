def compute(original_input):
    # copy of input
    input = [x for x in original_input]

    pointer = 0
    while(input[pointer] != 99):
        if input[pointer] == 1:
            input[input[pointer+3]] = input[input[pointer+1]] + input[input[pointer+2]]
        elif input[pointer] == 2:
            input[input[pointer+3]] = input[input[pointer+1]] * input[input[pointer+2]]
        else:
            raise ValueError('Wrong optocode')
        pointer += 4

    return input[0]


def main():
    input = open('input.txt', 'r').read().strip().split(',')
    input = [int(x) for x in input]

    output = 0
    noun = 0
    verb = -1
    # 4690667 -> 1202 Alarm state
    while noun < 100 and output != 19690720:
        verb += 1
        if verb > 99:
            verb = 0
            noun += 1
        input[1] = noun
        input[2] = verb
        output = compute(input)

    print("CODE IS: {0}".format(noun*100 + verb))


if __name__ == "__main__":
    main()
