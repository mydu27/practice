prod = 1
n = int(input('输入你想计算的阶乘'))
for i in range(1, n + 1):
    prod *= i
s = str(prod)
x1 = -1
x2 = 0
while -x1 <= n and s[x1] == '0':
    x1 = x1 - 1
    x2 = - x1 - 1
print(f'{n}的阶乘是{s}')
print(f'他的末尾有{x2}个0')