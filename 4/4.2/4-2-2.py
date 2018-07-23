def main():
    N = int(input('input a number you guess: '))
    t = 0
    for i in range(1, N+1):
        t += i
        print(i)
    print(f'三角数的值是：{t}')
    if t == N * (N + 1) / 2:
        print('三角数定理正确')
    else:
        print('不正确')


main()
