# phi表示黄金比例，它的倒数大致是0.6180333988，phi减去它的倒数，结果是1
def quad(a, b, c):
    determ = (b * b - 4 * a * c) ** 0.5
    x = (-b + determ) / (2 * a)
    return x


phi = quad(1, -1, -1)
print(phi)

x = 1 / phi
print(x)

if phi - 1 / phi == 1:
    print('成功')
