import random

name_list = ['google', 'tencent', 'taobao', 'baidu']


def search_substring():
    _str = 'abcdefgh'[random.randint(0, 7)]
    print(_str)
    for i in name_list:
        if _str in i:
            return i
        else:
            return 'not found'


for _ in range(10):
    print(search_substring())
