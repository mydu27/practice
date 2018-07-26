import random


def main():
    file_name = 'abcdefg'[random.randint(0, 6)] + '.txt'
    out_file = open(f'{file_name}', 'w')
    while True:
        s = input('Enter>>')
        if s in '@#￥%……&*':
            break
        out_file.write(s + '\n')
    out_file.close()
    return 'Done!'


print(main())
