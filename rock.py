import random

choices = ['rock', 'paper', 'scissors']


def play():
    computer_choice = random.choice(choices).lower()

    print(computer_choice)
    print('Rock, Paper, Scissor Go!')
    player_choice = input('enter your choice: ').lower()

    if player_choice not in choices:
        print('not a valid input, please enter correct choice \n')
        player_choice = input('enter your choice: ').lower()


    if computer_choice == player_choice:
        print('The game is drawed')

    # elif computer_choice == 'ROCK':
    #     if player_choice == 'PAPER':
    #         print('Player Wins!')
    #     else:
    #         print('Computer Wins!')
    elif computer_choice == 'rock' and player_choice == 'paper':
        print('Player Wins!')
    elif computer_choice == 'paper' and player_choice == 'scissors':
        print('Player Wins!')
    elif computer_choice == 'scissors' and player_choice == 'rock':
        print('Player Wins!')

    else:
        print('Computer Wins!')

play()

while input('do you want to go again (Y/N)').upper() == 'Y':
    play()