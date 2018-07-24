a = int(input('Enter a number: '))
sqr_list = [i * i for i in range(1, a + 1)]
format_str = '{:4} {:4} {:4}'
old_val = 0
for i, item in enumerate(sqr_list, 1):
    print(format_str.format(i, item, item - old_val))
    old_val = item
