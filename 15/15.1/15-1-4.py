emp_dict = {}

prompt = 'Select: 1. data entry, 2. query, 3. exit, 4. prefix>>'


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
        elif cmd == 4:
            display_by_prefix()


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
        print(emp_obj)
        if emp_obj is None:
            print('Name no found. Re-enter.')
        else:
            print('Dog Name:', emp_obj.dname)
            print('Strain:', emp_obj.strain)
            print('Host Name:', emp_obj.hname)
            print('age:', emp_obj.age)


def display_by_prefix():
    while True:
        s = input('Enter prefix(ENTER to exit):')
        s = s.strip()
        if not s:
            return
        for kv in emp_dict:
            if kv.startswith(s):
                emp_obj = emp_dict.get(kv)
                print('Dog Name:', emp_obj.dname)
                print('Strain:', emp_obj.strain)
                print('Host Name:', emp_obj.hname)
                print('age:', emp_obj.age)


def load_file():
    emp_dict.clear()
    while True:
        fname = input('Enter file to loaded:')
        in_file = open(fname, 'r')
        a_list = in_file.readlines()
        for i in range(0, len(a_list), 2):
            key_str = (a_list[i].strip('\n'))
            val_str = (a_list[i + 1]).strip('\n')
            emp_dict[key_str] = val_str
        return 'success loaded'
        in_file.close()
        break


def save_file():
    fname = input('Enter file to save')
    out_file = open(fname, 'w')
    for k in emp_dict:
        out_file.write(k + '\n')
        out_file.write(emp_dict[k] + '\n')
    out_file.close()


main()
