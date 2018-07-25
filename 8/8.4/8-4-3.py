def encode(a):
    a_list = []
    for ch in a:
        n = ord(ch) + 1
        if ch.isupper() and n > ord('Z'):
            n -= 26
        elif ch.islower() and n > ord('z'):
            n -= 26
        if ch.isalpha():
            a_list.append(chr(n))
        else:
            a_list.append(ch)
    s = ''.join(a_list)
    print('Coded string is', s)


def decode(a):
    b_list = []
    for ch in a:
        n = ord(ch) - 1
        if ch.isupper() and n < ord('A'):
            n += 26
        if ch.isalpha():
            b_list.append(chr(n))
        else:
            b_list.append(ch)
    s = ''.join(b_list)
    print('Coded string is', s)


def say_bye():
    print('good bye')


def main():
    while True:
        input_str = input('Enter string : ')
        if input_str == '':
            say_bye()
            break
        else:
            ask_word = input('Do you want to encode or decode?')
            if ask_word == 'encode':
                encode(input_str)
            elif ask_word == 'decode':
                decode(input_str)
            elif ask_word == '':
                say_bye()
                break


main()
