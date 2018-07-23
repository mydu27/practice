import random


def random_count():
    n = random.randint(1, 10)
    return n


def main():
    n = random_count()
    while True:
        print('anytime you want to exit you can input 0')
        ans = int(input('Enter your guess: '))
        if ans == n:
            print('Success! You win! Play it again!')
            main()
        elif ans > n:
            print('Too high.')
        elif ans == 0:
            print('Exit the game')
            break
        else:
            print('Too low.')


main()
