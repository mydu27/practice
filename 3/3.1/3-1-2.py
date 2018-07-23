def quad(a, b, c):
    determ = (b * b - 4 * a * c) ** 0.5
    x1 = (-b + determ) / 2 * a
    x2 = (-b - determ) / 2 * a
    print(f'The x1 value is {x1}')
    print(f'The x2 value is {x2}')


quad(1, -3, 2)
