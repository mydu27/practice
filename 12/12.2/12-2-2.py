import random

phone_dict = {}


def display_by_prefix():
    while True:
        s = input('Enter prefix (ENTER to exit):')
        s = s.strip()
        if not s:
            return
        name_list = [(k, v) for k, v in phone_dict.items()]
        name_list.sort()
        for k, v in name_list:
            if k.startswith(s):
                print(k, '\t', v)


def add_entries():
    while True:
        key_str = input('Input name (ENTER to exit):')
        key_str = key_str.strip()
        if not key_str:
            return
        val_str = input('Enter phone no: ')
        val_str = val_str.strip()
        if not val_str:
            return
        phone_dict[key_str] = val_str


def display_entries():
    if len(phone_dict) == 0:
        print('your phone dict is empty')
    else:
        while True:
            key_str = input('Enter name (ENTER to exit):')
            key_str = key_str.strip()
            if not key_str:
                return
            val_str = phone_dict.get(key_str)
            if val_str:
                return val_str
            else:
                return 'Name not found. Re-enter.'


def main():
    while True:
        prompt = 'Enter command:\n1. data entry,'
        prompt += '2. query, 3. exit, 4. prefix >>'
        print(prompt)
        s = random.randint(1, 4)
        if s == 3:
            break
        if s == 1:
            add_entries()
        elif s == 2:
            display_entries()
        elif s == 4:
            display_by_prefix()


main()
