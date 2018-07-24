# 打印2-n内的所有质数
n = int(input('Enter a number: '))
comp_list = [j for i in range(2, n)
             for j in range(i * i, n, i)]
prime_list = [i for i in range(2, n)
              if i not in comp_list]
print(prime_list)
