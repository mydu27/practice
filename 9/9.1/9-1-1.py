# 可以接受输入形如x，y和（x，y）的点
def main():
    x1, y1 = get_point()
    x2, y2 = get_point()
    dist, sum = calc_pts(x1, y1, x2, y2)
    print('The distance between points is:', dist)
    print('The sum of the point is:', sum)


def get_point():
    s = input('Enter point in "x, y" format:')
    s = s.strip('()')
    a_list = s.split(',')
    a = int(a_list[0].strip(''))
    b = int(a_list[1].strip(''))
    return a, b


def calc_pts(x1, y1, x2, y2):
    dist1 = y2 - y1
    dist2 = x2 - x1
    dist = (dist1 ** 2 + dist2 ** 2) ** 0.5
    sum = (x1 + x2, y1 + y2)
    return dist, sum


if __name__ == '__main__':
    main()
