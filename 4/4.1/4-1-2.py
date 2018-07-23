def main():
    your_number = int(input('think a number and input it: '))
    if not (your_number < 1 or your_number > 100):
        print('你输入的数字在1-100之间')
    else:
        print('你输入的数字不在1-100之间')


main()
