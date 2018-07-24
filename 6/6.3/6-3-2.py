n = int(input('Enter a number: '))
comp_list = [j for i in range(2, n)
             for j in range(i * i, n, i)]
prime_list = []
for i in range(2, n):
    if i not in comp_list:
        prime_list.append(i)
print(prime_list)
