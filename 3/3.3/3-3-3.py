# 计算直角三角形的面积，并在句尾加.
def main():
    height = float(input('Enter the height of square:'))
    width = float(input('Enter the width of square:'))
    area = height * width * 0.5
    fss = 'The distance is {}.'
    out_str = fss.format(area)
    print(out_str)


main()
