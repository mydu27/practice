# import random


# def main():
#     out_file = open('stuff.txt', 'w')
#     s = 'abcd'[random.randint(0, 3)]
#     out_file.write(s)
#     out_file.close()
#     return 'Done!'


# print(main())
def main():
    out_file = open('stuff.txt', 'w')
    while True:
        s = input('Enter>>')
        if not s:
            break
        out_file.write(s + '\n')
    out_file.close()
    return 'Done!'


print(main())
