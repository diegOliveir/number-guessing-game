import random
import math

print('Bem vindo ao jogo de adivinhação de números! \nPrimeiramente você irá selecionar um intervalo entre dois números inteiros e o sistema irá gerar um número aleatório que fique entre os dois(incluindo os mesmos). Você terá uma quantidade limitada de tentativas para acertar. \nBoa sorte!')

while True:
    try:
        lower_bound = int(input('Digite o menor número inteiro do intervalo: '))
        upper_bound = int(input('Digite o maior número inteiro do intervalo: '))

        if lower_bound > upper_bound:
            print('O menor número deve ser menor que o maior número.')
            continue
        break
    except ValueError:
        print('Digite somente números.')

number_to_guess = random.randint(lower_bound, upper_bound)
chances = math.log2(upper_bound - lower_bound - 1)
chances = round(chances)
guess_counter = 0

print(f'Você tem {chances} chances!')

while guess_counter < chances:
    try:
        my_guess = int(input('Dê o seu palpite: '))
    except ValueError:
        print('Digite somente números.')
        continue

    guess_counter += 1

    if my_guess == number_to_guess:
        print(f'Parabéns! Você acertou com {guess_counter} tentativa/s!')
        break
    elif guess_counter >= chances and my_guess != number_to_guess:
        print(f'Sinto muito, suas tentativas acabaram! O número era {number_to_guess}.')
        break
    elif my_guess > number_to_guess:
        print(f'Você chutou alto demais! Lhe restam {chances - guess_counter} tentativas.')
    elif my_guess < number_to_guess:
        print(f'Você chutou baixo demais! Lhe restam {chances - guess_counter} tentativas.')
