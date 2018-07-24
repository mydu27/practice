n = int(input('输入大于1的整数上限: '))
nums = range(1, n + 1)
format_str = '{:4} {:4} {:4}'
trips = [(a, b, c) for a in nums for b in nums for
         c in nums if a * a + b * b == c * c]
for a, b, c in trips:
    print(format_str.format(a, b, c))
