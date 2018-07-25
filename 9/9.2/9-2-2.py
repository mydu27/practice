def main():
    amt = 0
    while True:
        b, n = get_num()
        if not b:
            break
        amt += n
    print('The total is', amt)


def get_num(num=0.0):
    s = input('Input number (Enter to quit): ')
    if not s:
        return False, num
    else:
        return True, float(s)


if __name__ == '__main__':
    main()
