input_str = input('Enter string : ')
ask_word = input('Do you want to encode or decode?')
a_list = []
if ask_word == 'encode':
    for ch in input_str:
        n = ord(ch) + 1
        if ch.isupper() and n > ord('Z'):
            n -= 26
        elif ch.islower() and n > ord('z'):
            n -= 26
        if ch.isalpha():
            a_list.append(chr(n))
        else:
            a_list.append(ch)
elif ask_word == 'decode':
    for ch in input_str:
        n = ord(ch) - 1
        if ch.isupper() and n < ord('A'):
            n += 26
        if ch.isalpha():
            a_list.append(chr(n))
        else:
            a_list.append(ch)
s = ''.join(a_list)
print('Coded string is', s)
