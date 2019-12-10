from random import random, randrange

mode = ''
players = int(input('hoeveel  spelers zijn er: '))
while players < 2 or players > 6:
    print('je kan maar met 2 tot 6 spelers spelen')
    players = int(input('hoeveel  spelers zijn er: '))
c = 0
playernames = []
while c < players:
    playernames.append(input('your name: '))
    c += 1
print(playernames)
while mode != 'basic' and mode != 'advanced':
    a = input('kies je mode basic of advanced: ')
    mode = a

print(mode)
if mode == 'basic':
    goal = 50
else:
    goal = 100

ans = ''
score = []
playerscore = []
currentroll = 0
c2 = 0
for i in range(len(playernames)):
    score.append(0)
    # print(playernames[i]) # placeholder for my turn function
    playerscore = [playernames, score]
done = ''
while done != 'done':

    for i in range(len(playernames)):
        if done == 'done':
            break
        else:
            print(playerscore[0][i], playerscore[1][i])
            ans = ''

            while ans != 'pass' or c2 < 0:
                ans = (input('press r to roll or p to pass: '))

                if ans == 'r':
                    random = randrange(1, 6)
                    print(random)
                    currentroll = currentroll + random
                    print(playerscore[0][i], 'heeft ', playerscore[1][i], ' punten. zoveel punten kan je erbij toevoegen: ', currentroll)
                    c2 = c2 + 1
                    if random == 1:
                        currentroll = currentroll - currentroll
                        print(playerscore[0][i], ' heeft 1 gerolled score is nu: ', playerscore[1][i])
                        ans = 'pass'
                if ans == 'p':
                    playerscore[1][i] = playerscore[1][i] + currentroll
                    currentroll = currentroll - currentroll
                    ans = 'pass'
                    if playerscore[1][i] >= goal:
                        done = 'done'
                        print('the game is finished ', playerscore[0][i], ' heeft gewonnen')

                else:
                    print('press r or p')

