fib_list = [1, 2, 4, 5, 8, 13, 21, 34, 55, 89, 144]
format_str = '{:3} {:5} {:5}'
a = 4
for i, item in enumerate(fib_list, 1):
    if i >= 3:
        print('{:3} {:5} {:5}'.format(i, item, item - a))
        a = item
