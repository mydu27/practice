in_str = input('Enter items: ')
a_list = in_str.split(',')
a_list.sort()
print('Here is the secord list...')
for s in a_list:
    s = s.strip()
    print(s, end=' ')
