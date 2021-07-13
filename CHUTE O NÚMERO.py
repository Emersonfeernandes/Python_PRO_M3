import random

x = random.randint(1,10)

while True:
   
    a = int(input('Digite um número de 1 a 10: '))

    if x > a:
        print('Você chutou baixo!')
    elif x < a:
        print('Você chutou alto!')
    elif x == a:
        print(f'Parabéns o número é {a}, você acertou!')
        break
