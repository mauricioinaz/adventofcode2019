def next_increase(numb):
    pointer = -1
    if numb[pointer] == '9':
        while numb[pointer] == '9':
            pointer -= 1
        # make all numbers equal after pivot to next increment
        # ie 359999 -> 366666
        return numb[:pointer] + str(int(numb[pointer])+1)*abs(pointer)
    else:
        return str(int(numb)+1)


def has_doubles(numb):
    return len(set(numb)) < len(numb)


def main():
    lower_limit = 359999  # This might me cheating :( should be 359282
    upper_limit = 820401

    n = str(lower_limit)
    number_of_passwords = 0
    while int(n) < upper_limit:
        n = next_increase(n)
        if has_doubles(n):
            number_of_passwords += 1

    print(number_of_passwords)


if __name__ == "__main__":
    main()
