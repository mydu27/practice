input_str = input('Enter input string: ')
output_str = input_str.upper()
a_list = [ch for ch in output_str if ch.isalpha()]
s = ''.join(a_list)
print(s)
