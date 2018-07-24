nums = range(1, 11)
trips = [(a, b, c, d) for a in nums for b in nums for
         c in nums for d in nums if a * a + b * b + c * c == d * d]
print(trips)
