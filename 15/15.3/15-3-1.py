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


def is_linear(t):
    p1, p2, p3 = t
    return p3 - p2 == p2 - p1


all_pts = [Point3D(a, b, c) for a in range(3) for b in range(3)
           for c in range(3)]

n = len(all_pts)
print('The number of positions is', n)
combos = [(all_pts[i], all_pts[j], all_pts[k]) for i in range(n)
          for j in range(i + 1, n) for k in range(j + 1, n)]
my_combos = [i for i in combos if is_linear(i)]
print('Number of winning combos is', len(my_combos))
