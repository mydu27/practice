import random


def random_count(a, b):
    n = random.randint(a, b)
    return n


def main():
    a = int(input('input your begin number：'))
    b = int(input('input your finish number：'))
    n = random_count(a, b)
    while True:
        print('anytime you want to exit you can input 0, let it go!')
        ans = int(input('Enter your guess: '))
        if ans == n:
            print('Success! You win! Play it again or 0 exit!')
            main()
        elif ans > n:
            print('Too high.')
        elif ans == 0:
            print('Exit the game')
            break
        else:
            print('Too low.')


main()
