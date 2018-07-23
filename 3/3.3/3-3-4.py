from math import pi


def main():
    r = float(input('输入想计算的圆的半径：'))
    area = 0.5 * pi * r ** 2
    fss = 'The distance is {}.'
    out_str = fss.format(area)
    print(out_str)


main()