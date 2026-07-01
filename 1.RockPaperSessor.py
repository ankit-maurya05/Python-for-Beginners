import random


def get_choices():

    player_choice = input('Enter a choice (rock, paper, scissor)-->')
    options = ['rock','paper','sissor']
    computer_choice = random.choice(options)
    choices = {'player':player_choice,
              'computer':computer_choice}
    return choices

def cheak_win(player,computer):
    print(f'you chose {player} and computer chose {computer}')
    if player==computer:
        return "Its a tie!"
    elif player=='rock' and computer=='sissor':
        return "player win!"
    elif player == "sissor" and computer == 'paper':
        return 'player win!'
    elif player == "paper" and computer == "rock":
        return "player win!"
    else:
        return "computer win!"
    
choices=get_choices()
winner=cheak_win(choices['player'],choices['computer'])

print(winner)

