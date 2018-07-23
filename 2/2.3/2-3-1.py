# 求解二元一次方程的另一个解
a = 5
b = 4
c = 3
determ = (b * b - 4 * a * c) ** 0.5
x = (-b - determ) / 2 * a
print(x)