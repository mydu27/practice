class Polygon:
    pi = 3.14159265

    @staticmethod
    def get_area(factors, sides, cfacts):
        data = []
        for name in sides:
            x = float(input(' Enter ' + name + ': '))
            data.append(x)
        prod = 1
        for i in factors:
            prod *= data[i - 1]
        for i in cfacts:
            prod *= i
        return prod


class Square(Polygon):
    def __init__(self):
        self.a = Polygon.get_area([1, 1], ['side'], [])


class Rectangle(Polygon):
    def __init__(self):
        self.a = Polygon.get_area([1, 2], ['height', 'width'], [])


class Sphere(Polygon):
    def __init__(self):
        self.v = Polygon.get_area([1, 1, 1], ['radius'], [Polygon.pi, 4/3])


class Cylinder(Polygon):
    def __init__(self):
        self.v = Polygon.get_area([1, 1, 2], ['radius', 'height'],
                                  [Polygon.pi])


class Pyramid(Polygon):
    def __init__(self):
        self.v = Polygon.get_area([1, 2], ['prism', 'height'], [1/3])


print('The area of a square...')
a_square = Square()
print('The area of a square is', a_square.a)

print('The area of a rectangle...')
a_rect = Rectangle()
print('The area of a rectangle is', a_rect.a)

print('The volum of a sphere...')
a_sphere = Sphere()
print('The volum of a sphere is', a_sphere.v)

print('The volum of a cylinder...')
a_cylinder = Cylinder()
print('The volum of a cylinder is', a_cylinder.v)

print('The volum of a pyramid...')
a_pyramid = Pyramid()
print('The volum of a pyramid is', a_pyramid.v)
