def main():
    while True:
        fname = input('Enter file name: ')
        if not fname:
            return False
        try:
            if open_file(fname):
                continue
        except FileNotFoundError:
            print('File not be found .Re-enter.')


def open_file(fname):
        if not fname:
            return False
        else:
            fss = '{:>2}. {}'
            in_file = open(fname)
            str_list = in_file.readlines()
            for i, item in enumerate(str_list):
                print(fss.format(i, item), end='')
            in_file.close()
            return True


main()
