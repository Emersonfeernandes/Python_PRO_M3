import random

while True:
    x = random.randint(1,6)
    print('Você quer jogar o dado?')
    try:
        y = int(input('1 para não ou 2 para sim: '))
    except ValueError:
        print('Por favor digite 1 e 2 como sim ou não.')
        continue

    if y == 1:
        print()
        print(f'O número sorteiado foi: {x}')
        print()
    else:
        print('Fim do jogo!')
        break
