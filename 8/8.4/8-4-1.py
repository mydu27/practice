input_str = input('Enter string to decode: ')
input_num = int(input('Enter decode number you want: '))
a_list = []
m = input_num % 25
for ch in input_str:
    n = ord(ch) - m
    if ch.isupper() and n < ord('A'):
        n += 26
    if ch.isalpha():
        a_list.append(chr(n))
    else:
        a_list.append(ch)
s = ''.join(a_list)
print('Coded string is', s)
