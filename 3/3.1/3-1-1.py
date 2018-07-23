def quad(a, b, c):
    x = (b * b - 4 * a * c) ** 0.5
    x1 = (-b + x) / (2 * a)
    return x1


print(quad(1, 2, 1))
