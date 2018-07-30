in_file = None


def main():
    if open_file():
        fss = '{:>6}. {}'
        str_list = in_file.readlines()
        for i, item in enumerate(str_list, 1):
            print(fss.format('>>' + str(i), item), end='')
        in_file.close()


def open_file():
    global in_file
    while True:
        try:
            fname = input('Enter file name: ')
            if not fname:
                return False
            in_file = open(fname)
            return True
        except FileNotFoundError:
            print('File not be found .Re-enter.')


main()
