class Point3D:
    # 表示三维点的类，支持加法和比较运算
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, other):
        d1 = self.x - other.x
        d2 = self.y - other.y
        d3 = self.z - other.z
        return Point3D(d1, d2, d3)

    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y and self.z == other.z)


def main():
    s = ''
    while not s or s[0] in 'Yy':
        p1 = get_point()
        p2 = get_point()
        p3 = get_point()
        if is_win(p1, p2, p3):
            print('Is a winning combination.')
        else:
            print('Is not a win')
        s = input('Do again(Y or N)')


def get_point():
    s = input('Enter point in x, y, z:')
    ls = s.split(',')
    x, y, z = int(ls[0]), int(ls[1]), int(ls[2])
    return Point3D(x, y, z)


def is_win(p1, p2, p3):
    if (p3 - p2 == p2 - p1 or p2 - p3 == p3 - p1 or p3 - p1 == p1 - p2):
        # if (p1 == p2 or p1 == p3 or p2 == p3):
        #     return False
        # else:
        return True
    else:
        return False


main()
