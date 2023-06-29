from emoji import emojize
from random import choice
opcoes = ['PEDRA', 'PAPEL', 'TESOURA']
computador = choice(opcoes)
print(emojize('\033[34m=============OPÇÕES===========\n1      -     PEDRA         :fist:\n2      -     PAPEL         :hand:\n3      -     TESOURA       :v:', language='alias'))
jogador = int(input('\033[33mEscolha uma opção: \033[m'))
print(f'\033[34m{"="*30}\n\033[33mO computador escolheu \033[35m{computador}' if jogador in [1, 2, 3] else f'\033[34m{"="*30}\n\033[31mOpção inválida - Tente novamente!')
if jogador == 1:
    print(f'\033[33mVocê escolheu \033[35mPEDRA\n\033[34m{"="*30}')
    if computador == 'PEDRA':
        print(f'\033[33m{"Empate":^30}')
    elif computador == 'PAPEL':
        print(f'\033[31m{"Você perdeu":^30}')
    else:
        print(f'\033[32m{"Você ganhou":^30}')
elif jogador == 2:
    print(f'\033[33mVocê escolheu \033[35mPAPEL\n\033[34m{"="*30}')
    if computador == 'PEDRA':
        print(f'\033[32m{"Você ganhou":^30}')
    elif computador == 'PAPEL':
        print(f'\033[33m{"Empate":^30}')
    else:
        print(f'\033[31m{"Você perdeu":^30}')
elif jogador == 3:
    print(f'\033[33mVocê escolheu \033[35mTESOURA\n\033[34m{"="*30}')
    if computador == 'PEDRA':
        print(f'\033[31m{"Você perdeu":^30}')
    elif computador == 'PAPEL':
        print(f'\033[32m{"Você ganhou":^30}')
    else:
        print(f'\033[33m{"Empate":^30}')
