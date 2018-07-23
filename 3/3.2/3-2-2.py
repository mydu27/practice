# 修改后，用户必须输入整数值
def main():
    a = int(input('Enter the value of the x-square coefficient: '))
    b = int(input('Enter the value of the x coefficient: '))
    c = int(input('Enter the value of the constant: '))
    determ = (b * b - 4 * a * c) ** 0.5
    x1 = (-b + determ) / (2 * a)
    x2 = (-b - determ) / (2 * a)
    print('Answer are', x1, 'and', x2)


main()
