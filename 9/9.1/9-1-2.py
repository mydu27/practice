def get_number():
    s = input('输入4个数字，并用空格隔开每个数字：')
    a_list = s.split(' ')
    a = float(a_list[0].strip())
    b = float(a_list[1].strip())
    c = float(a_list[2].strip())
    d = float(a_list[3].strip())
    return a, b, c, d


def calculate_number(a, b, c, d):
    sum = a + b + c + d
    average = sum / 4
    return sum, average


def main():
    a, b, c, d = get_number()
    sum, average = calculate_number(a, b, c, d)
    print(f'你输入数字的和是：{sum}')
    print(f'你输入数字的平均值是：{average}')


if __name__ == '__main__':
    main()
