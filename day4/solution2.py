def incremental(numb):
    sorted_numb_str = ''.join(sorted(str(numb)))
    return str(numb) == sorted_numb_str


def has_doubles(number):
    numb = str(number)
    for n in numb:
        if numb.count(n) == 2:
            return True
    return False


def main():
    lower_limit = 359282
    upper_limit = 820401

    n = lower_limit
    number_of_passwords = 0
    while n < upper_limit:
        if incremental(n) and has_doubles(n):
            number_of_passwords += 1
        n += 1

    print(number_of_passwords)


if __name__ == "__main__":
    main()
