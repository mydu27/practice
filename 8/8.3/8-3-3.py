input_str = input('Enter string to encode: ')
input_count = int(input('Enter a number: '))
a_list = []
if input_count > 25:
    input_count = input_count % 24
for ch in input_str:
    n = ord(ch) + input_count
    if ch.isupper() and n > ord('Z'):
        n = n - 26
    elif ch.islower() and n > ord('z'):
        n = n - 26
    if ch.isalpha():
        a_list.append(chr(n))
    else:
        a_list.append(ch)
s = ''.join(a_list)
print('Coded string is', s)
