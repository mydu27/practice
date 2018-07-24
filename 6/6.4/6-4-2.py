nums = range(1, 11)
all_nums = [(a * a, b * b, a * a + b * b) for a in nums
            for b in nums if a * a + b * b < 100]
print(all_nums)
