def get_fuel(mass):
    calc = (int(mass) // 3) - 2
    if calc < 0:
        return 0
    return calc + get_fuel(calc)


def main():
    lines = list(open('input.txt', 'r'))
    result = 0

    for line in lines:
        result += get_fuel(line)

    print(result)


if __name__ == "__main__":
    main()
