# 不使用全局变量
j_str = '''John Lennon. Witty, cheeky, sasssy. You like
           to be the leader of your own band.'''
p_str = '''Paul McCartney. You are popular, likable, and
           charismatic. You make a great impression.'''
g_str = '''George Harrison. You are serious, reflective,
           and deeply committed to your work.'''
r_str = '''Ringo Starr. You are lovable and just want
           everyone to get along.'''


def main():
    a = ask_q(
        'Are you more Assertive or Supportive?', 'AS')
    if a == 'A':
        b = are_assertive()
    else:
        b = are_supportive()
    print('You are a', b)


def are_assertive():
    a = ask_q(
        'Are you more Intellectual or Social?', 'IS')
    if a == 'I':
        b = j_str
    else:
        b = p_str
    return b


def are_supportive():
    a = ask_q(
        'Are you more Intellectual or Social?', 'IS')
    if a == 'I':
        b = g_str
    else:
        b = r_str
    return b


def ask_q(msg, choices):
    while True:
        s = input(msg)
        s = s.upper()
        if s and s[0] in choices:
            return s[0]
        else:
            print('Enter one of the choices.')
            print('First letter is sufficient.')


main()
