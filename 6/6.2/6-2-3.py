# 重写6-2-2，避免使用其外部声明的变量
a = int(input('Enter a number: '))
sqr_list = [i ** 3 for i in range(1, a + 1)]
format_str = '{:4} {:4} {:4}'
for i, item in enumerate(sqr_list, 1):
    if i >= 2:
        print(format_str.format(i, item, item - sqr_list[i - 2]))
        old_val = item
