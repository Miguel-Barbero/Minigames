import random
def one_play():
    player=[random.randint(1,10),random.randint(1,10)]
    npc=[random.randint(1,10),random.randint(1,10)]
    print('You have a',player[0],'and a',player[1],'Total:',sum(player))
    while True:
        draw=input('Do you want another card (Yes or No)?: ')
        if draw=='Yes':
            card=random.randint(1,10)
            player.append(card)
            print('You got a', card, 'total: ', sum(player))
        elif draw=='No':
            break
        else:
            print('Only Yes or No entries are accepted')
            continue
    while sum(npc)<18:
        npc.append(random.randint(1,10))
    print('Your cards are: ', player,'Toal:', sum(player))
    print('Your rival´s cards are:',npc,'Total:',sum(npc))
    if sum(player)>21:
        if sum(npc)>21:
            print('You both lose')
        else:
            print('Your rival wins')
    elif player[0]==1 and player[1]==3 and player[2]==5 and player[3]==8:
        if npc[0]==1 and npc[1]==3 and npc[2]==5 and npc[3]==8:
            print('Ultra draw')
        else:
            print('You ultra win')
    else:
        if npc[0]==1 and npc[1]==3 and npc[2]==5 and npc[3]==8:
            print('You ultra lose')
        elif sum(player)==sum(npc):
            print('Draw')
        elif sum(npc)>sum(player) and sum(npc)<=21:
            print('You lose')
        else:
            print('You win')
def blackjack():
    print('Welcome to pyBlackJack by SunSeT. Get a 1,3,5 and 8 (in that order) for an automatic victory')
    one_play()
    while True:
        re=input('Do you want to play again?(Yes or No): ')
        if re=='Yes':
            one_play()
        elif re=='No':
            print('Than you for playing')
            quit()
        else:
            print('Only Yes or No entries are accepted')
            continue
blackjack()
