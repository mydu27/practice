phone_dict = {}


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
            add_entries()
        elif cmd == 2:
            display_entries()


def add_entries():
    while True:
        key_str = input('Input name (ENTER to exit):')
        key_str = key_str.strip()
        if not key_str:
            return
        val_str = input('Enter phone no:')
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
                print(val_str)
            else:
                print('Name not found. Re-enter.')


main()
