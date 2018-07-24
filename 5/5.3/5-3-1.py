def input_number():
    a = int(input('The upper limit you want to set up: '))
    return a


def main():
    b = input_number()
    bool_list = [True] * int(b)
    for prime in range(2, b):
        if bool_list[prime]:
            print(prime, end=' ')
            for i in range(prime * 2, b, prime):
                bool_list[i] = False


main()
