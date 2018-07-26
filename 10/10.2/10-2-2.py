import random

rom_list = [('M', 1000), ('CM', 900), ('D', 500),
            ('CD', 400), ('C', 100), ('XC', 90),
            ('XL', 40), ('X', 10), ('IX', 9),
            ('V', 5), ('IV', 4), ('I', 1)]

amt = 0

rim_list = []


def make_roman(letter, n):
    global amt
    while amt >= n:
        amt = amt - n
        rim_list.append(letter)
    return rim_list


def main():
    global amt
    amt = random.randint(1, 1000)
    print(amt)
    # print('The Roman number is:')
    for item in rom_list:
        make_roman(item[0], item[1])
    s = ''.join(rim_list)
    return s


if __name__ == '__main__':
    print(f'The Roman number is: {main()}')
