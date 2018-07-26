import random

N = random.randint(3, 100)
nums = set(range(2, N))
comps = {j for i in nums for j in range(i * i, N, i)}
print(nums - comps)
