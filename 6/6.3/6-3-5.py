evens_list = [j for j in range(1, 21)
              if j % 2 == 0]

odds_list = [i for i in range(1, 21)
             if i not in evens_list]
print(f'偶数列表是：{evens_list}')
print(f'奇数列表是：{odds_list}')
