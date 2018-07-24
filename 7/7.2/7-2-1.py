while True:
    n = int(input('Enter number to calc. factorial for:'))
    if n == 0:
        break
    else:
        prod = 1
        for i in range(1, n + 1):
            prod *= i
        s = str(prod)
        z = len(s) - len(s.strip('0'))
        print(n, 'factorial is', s)
        print('The number of trailing zeros is', z)