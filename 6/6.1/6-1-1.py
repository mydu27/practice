# 使用range函数生成和enumerate函数同样的输出
fib_list = [1, 2, 4, 5, 8, 13, 21, 34, 55, 89, 144]
for i in range(1, len(fib_list) + 1):
    print('{:>2}. {:>4}'.format(i, fib_list[i-1]))
