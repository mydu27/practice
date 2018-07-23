# 根据输入的球形半径计算其体积
def main():
    r = float(input('The radius of the ball you want to calculate: '))
    pi = 3.14159265
    area = (4 * pi * r ** 3) / 3
    print(f'The area of the ball is {area}')


main()
