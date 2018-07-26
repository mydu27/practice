# 用集合找出1-25的所有偶数和奇数
nums = set(range(1, 26))
even_number = {i for i in nums if i % 2 == 0}
print(even_number, '\n', nums - even_number)
