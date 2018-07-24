a_list = []
while True:
    str1 = input('Enter a name: ')
    if str1 == '':
        break
    a_list.append(str1)
print(f'all the name you input is {len(a_list)}.')
a_list.sort()
print('Here is the alpha sorted list...')
for str1 in a_list:
    print(str1, end=' ')
