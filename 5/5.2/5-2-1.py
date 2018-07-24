# 计算n的阶乘，输入0退出
while True:
    n = int(input('Calculate factorial for which n? or 0 to exit: '))
    prod = 1
    if n == 0:
        print('finish calculate')
        break
    else:
        for i in range(n):
            prod *= i + 1
        print(f'The result is: {prod}')
