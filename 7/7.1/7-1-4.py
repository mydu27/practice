while True:
    n = int(input('输入你想计算的阶乘：'))
    prod = 1
    if n == 0:
        break
    else:
        for i in range(1, n + 1):
            prod *= i
        s = str(prod)
        x1 = len(s)
        x2 = 0
        while x1 > 0 and s[x1 - 1] == '0':
            x2 = x2 + 1
            x1 = x1 - 1
        print(f'{n}的阶乘是{s}')
        print(f'他的末尾有{x2}个0')