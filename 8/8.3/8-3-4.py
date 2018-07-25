input_str = input('Enter string to encode: ')
a_list = []
for ch in input_str:
    if ch.isalpha:
        n = ord(ch) + 1
        a_list.append(chr(n))
s = ''.join(a_list)
print('Coded string is', s)
