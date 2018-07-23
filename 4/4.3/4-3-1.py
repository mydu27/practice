def main():
    a = b = 1
    count_list = []
    n = int(input('输入一个数字n：'))
    while a < n:
        a, b = a + b, a
        count_list.append(b)
        coun_list = count_list[1:]
    for i in coun_list:
        print(i)


main()
