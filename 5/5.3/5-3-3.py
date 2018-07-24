from math import sqrt


def input_number():
    a = int(input('The upper limit you want to set up: '))
    return a


def main():
    # 求2到a之间的所有素数
    x1 = 2
    a = input_number()
    length_list = []
    while x1 <= a:
        i = 2
        b = sqrt(x1)
        while i <= b:
            if x1 % i == 0:
                break
            i = i+1
        if i > b:
            print(x1, end=' ')
            length_list.append(x1)
        x1 = x1 + 1
    print(f'一共找到了{len(length_list)}个质数')


main()
