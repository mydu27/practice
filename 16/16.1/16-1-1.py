# 16-1-1和16-1-2写在一起
class PointN:
    def __init__(self, *args):
        if isinstance(args[0], list):
            self.the_list = [i for i in args[0]]
        else:
            self.the_list = [i for i in args]
        self.list_len = len(self.the_list)

    def __str__(self):
        al_list = [str(i) for i in self.the_list]
        return 'point(' + ', '.join(al_list) + ')'

    def __add__(self, other):
        new_list = []
        n = min(self.list_len, other.list_len)
        for i in range(n):
            new_list.append(self.the_list[i] + other.the_list[i])
        return PointN(new_list)

    def __sub__(self, other):
        new_list = []
        n = min(self.list_len, other.list_len)
        for i in range(n):
            new_list.append(self.the_list[i] - other.the_list[i])
        return PointN(new_list)

    def __mult__(self, n):
        new_list = []
        m = self.list_len
        for i in range(m):
            new_list.append(self.the_list[i] * n)
        return PointN(new_list)


pt1 = PointN(1, 2, 3, 4)
a_list = [10, 10, 10, 10]
pt2 = PointN(a_list)
n = PointN(2)
print('pt1 is', pt1)
print('pt2 is', pt2)
print('Sum is', pt2 * n)
