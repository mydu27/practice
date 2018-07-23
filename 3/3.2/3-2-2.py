# 修改后，用户必须输入整数值
def answer(x):
    if not x.isdigit():
            print('your input has mistake')
            main()


def main():
    a = input('Enter the value of the x-square coefficient: ')
    answer(a)
    b = input('Enter the value of the x coefficient: ')
    answer(b)
    c = input('Enter the value of the constant: ')
    answer(c)
    determ = (int(b) * int(b) - 4 * int(a) * int(c)) ** 0.5
    x1 = (-int(b) + determ) / (2 * int(a))
    x2 = (-int(b) - determ) / (2 * int(a))
    print('Answer are', x1, 'and', x2)


main()
