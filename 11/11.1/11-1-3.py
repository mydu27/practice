def main():
    out_file = open('stuff.txt', 'w')
    while True:
        s = input('Enter>>')
        if not s:
            break
        s = write_line(s)
        out_file.write(s)
    out_file.close()
    return 'Done!'


def write_line(s):
    s = s + '\n'
    return s


print(main())
