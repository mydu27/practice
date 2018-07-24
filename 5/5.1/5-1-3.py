a_list = []
while True:
    x1 = input('Enter a number: ')
    if x1 == '':
        break
    a_list.append(float(x1))
print(f'all the number you input is {len(a_list)}.')
a_list.sort()
print('Here is the alpha sorted list...')
for str1 in a_list:
    print(str1, end=' ')
