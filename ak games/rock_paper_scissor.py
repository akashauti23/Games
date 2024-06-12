import random

options = ['rock', 'paper', 'scissor']


def get_user_choice():
    print('Choose one of the following:')
    print('1. Rock')
    print('2. Paper')
    print('3. Scissor')
    choice = int(input('Enter your choice: '))
    return options[choice - 1]


def get_computer_choice():
    return random.choice(options)


def get_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'draw'
    elif user_choice == 'rock' and computer_choice == 'scissor':
        return 'user'
    elif user_choice == 'scissor' and computer_choice == 'paper':
        return 'user'
    elif user_choice == 'paper' and computer_choice == 'rock':
        return 'user'
    else:
        return 'computer'
    

def main():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f'User choice: {user_choice}')
    print(f'Computer choice: {computer_choice}')
    winner = get_winner(user_choice, computer_choice)
    if winner == 'draw':
        print('It is a draw!')
    else:
        print(f'{winner} wins!')


if __name__ == '__main__':
    main()