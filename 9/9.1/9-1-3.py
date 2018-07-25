# 返回你输入所有数字的和与平均值
def calculate_count(list):
    a = 0
    for i in list:
        a += float(i)
    return a, a / len(list)


def main():
    s = input('输入数字，并用空格隔开每个数字：')
    a_list = s.split(' ')
    a, b = calculate_count(a_list)
    print(f'这些数字的和是：{a}')
    print(f'这些数字的平均值是：{b}')


if __name__ == '__main__':
    main()
