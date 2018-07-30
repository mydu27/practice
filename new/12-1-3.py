import random

score_dict = {}


def main():
    while True:
        prompt = 'Enter command:1. data entry, '
        prompt += '2. query, 3. exit >>'
        s = input(prompt)
        if not s:
            break
        cmd = int(s)
        if cmd == 3:
            break
        if cmd == 1:
            add_score()
        elif cmd == 2:
            display_score()


def add_score():
    while True:
        key_str = input('Input name (ENTER to exit):')
        key_str = key_str.strip()
        if not key_str:
            return
        val_str = random.uniform(1, 100)
        if not val_str:
            return
        score_dict[key_str] = val_str


def display_score():
    if len(score_dict) == 0:
        print('your score dict is empty')
    else:
        while True:
            key_str = input('Enter name (ENTER to exit):')
            key_str = key_str.strip()
            if not key_str:
                return
            val_str = score_dict.get(key_str)
            if val_str:
                print(val_str)
            else:
                print('Name not found. Re-enter.')


main()
