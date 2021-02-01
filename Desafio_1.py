'''Faça um script que gere o cruzamento de jogos entre cinco times, onde deve ser considerado jogo em casa e jogo na casa do adversário.'''

Times = ['Figueirense', 'Avaí', 'Flamengo', 'Palmeiras', 'Chapecoense']
for time1 in Times:
    for time2 in Times:
        if time1 != time2:
            print('{} x {}'.format(time1, time2))


