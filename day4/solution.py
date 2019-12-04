def get_next_increase(number):
    numb = str(number)
    pointer = -1
    if numb[pointer] == '9':
        while numb[pointer] == '9':
            pointer -= 1
        # make all numbers equal after pivot to next increment
        # ie 359999 -> 366666
        return int(numb[:pointer] + str(int(numb[pointer])+1)*abs(pointer))
    else:
        return int(numb)+1


def has_doubles(number):
    numb = str(number)
    for n in numb:
        if numb.count(n) == 2:
            return True
    return False


def main():
    lower_limit = 359999  # This might me cheating :( should be 359282
    upper_limit = 820401

    n = lower_limit
    number_of_passwords = 0
    while n < upper_limit:
        n = get_next_increase(n)
        if has_doubles(n):
            number_of_passwords += 1

    print(number_of_passwords)


if __name__ == "__main__":
    main()
