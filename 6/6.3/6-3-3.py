# 列表推导生成一个包含前十个三角数的列表
nums = [int((i * j + i) / 2) for i in range(1, 11) for j in range(1, 11)
        if i == j]

print(nums)
