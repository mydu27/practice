in_str = input('Enter items: ')
a_list = in_str.split(',')
a_list.sort()
print('Here is the secord list...')
my_string = ''
for s in a_list:
    my_string += s
print(my_string)
