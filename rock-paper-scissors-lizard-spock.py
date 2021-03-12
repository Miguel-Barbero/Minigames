import random
def rpsls():
    print('Welcome to the classic: Rock, paper, scissors, lizard, spock.')
    while True:
        player=input('Select: rock, paper, scissors, lizard o spock:')
        options=['rock','paper','scissors','lizard','spock']
        npc=random.choice(options)
        if player=='rock' or player=='paper' or player=='scissors' or player=='lizard' or player=='spock':
            print('You have chosen:',player)
            print('Your rival has chosen:',npc)
            if player==npc:
                print('Draw')
            elif player=='rock':
                if npc==options[3] or npc==options[2]:
                    print('You win')
                else:
                    print('You lose')
            elif player=='paper':
                if npc==options[0] or npc==options[4]:
                    print('You win')
                else:
                    print('You lose')
            elif player=='scissors':
                if npc==options[1] or npc==options[3]:
                    print('You win')
                else:
                    print('You lose')
            elif player=='lizard':
                if npc==options[1] or npc==options[4]:
                    print('You win')
                else:
                    print('You lose')
            elif player=='spock':
                if npc==options[0] or npc==options[2]:
                    print('You win')
                else:
                    print('You lose')
        else:
            print('Answer not supported')
        re=input('Do you want to play again? (Yes or No):')
        if re=='Yes':
            pass
        elif re=='No':
            print('Thank you for playing')
            break
        else:
            print('Only Yes or No answers are supported')
            continue
rpsls()