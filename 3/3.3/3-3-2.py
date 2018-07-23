# 在输出句子末尾加一个.
x1 = float(input('Enter x1: '))
x2 = float(input('Enter x2: '))
y1 = float(input('Enter y1: '))
y2 = float(input('Enter y2: '))
h = x2 - x1
v = y2 - y1
d = (h * h + v * v) ** 0.5
fss = 'The distance is {}.'
out_str = fss.format(d)
print(out_str)
