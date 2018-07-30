in_file = None


def main():
    if open_file():
        fss = '{:>4}. {}'
        str_list = in_file.readlines()
        s = input('Enter the begin line and end line:')
        a_list = s.split(',')
        for i, item in enumerate(str_list, 1):
            if int(a_list[1]) > int(a_list[0]) > 0 and int(a_list[1]) <= int(len(str_list)):
                if int(a_list[0]) <= i <= int(a_list[1]):
                    print(fss.format(i, item), end='')
            else:
                print('not found')
                break
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
