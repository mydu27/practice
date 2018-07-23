# 打印a/b的值，发现比值收敛到黄金比例，约1.618
def main():
    a = b = 1
    n = int(input('输入一个数字n：'))
    while a < n:
        a, b = a + b, a
        print(a / b)


main()
