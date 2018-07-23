# 修改后没必要修改变量的名称
def main():
    a = float(input('Enter the value of the x-square coefficient: '))
    b = float(input('Enter the value of the x coefficient: '))
    c = float(input('Enter the value of the constant: '))
    determ = (b * b - 4 * a * c) ** 0.5
    x1 = (-b + determ) / (2 * a)
    x2 = (-b - determ) / (2 * a)
    print('Answer are', x1, 'and', x2)


main()
