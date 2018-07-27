emp_dict = {}

prompt = 'Select: 1. data entry, 2. query, 3.exit>>'


class Employee:
    def __init__(self, dname, strain, hname, age):
        self.dname = dname
        self.strain = strain
        self.hname = hname
        self.age = age


def main():
    while True:
        s = input(prompt)
        if len(s) == 0:
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
        key_str = input('Input dog name(ENTER to exit):')
        key_str = key_str.strip()
        if not key_str:
            return
        strain = input('Enter dog strain:')
        hname = input('Enter host name:')
        age = int(input('Enter dog age:'))
        emp_dict[key_str] = Employee(key_str, strain, hname, age)


def display_entries():
    while True:
        key_str = input('Input dog name(ENTER to exit):')
        key_str = key_str.strip()
        if not key_str:
            return
        emp_obj = emp_dict.get(key_str)
        if emp_obj is None:
            print('Name no found. Re-enter.')
        else:
            print('Dog Name:', emp_obj.dname)
            print('Strain:', emp_obj.strain)
            print('Host Name:', emp_obj.hname)
            print('age:', emp_obj.age)


main()
