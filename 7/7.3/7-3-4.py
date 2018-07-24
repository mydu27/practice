in_str = input('Enter items: ')
a_list = in_str.split(',')
a_list.sort()
print('Here is the secord list...')
my_string = ''
for s in a_list:
    s = s.strip()
    my_string = my_string + s + ','
if len(my_string) >= 2:
    print(my_string[:-1])
