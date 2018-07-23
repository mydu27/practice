# 计算大于google且能被13整除的最小整数）
a = 13
google = 10 ** 100
while True:
    google % a != 0
    google += 1
    if google % a == 0:
        print(google)
        break
