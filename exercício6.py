import random

print('Exercício 6 - Jogo do par ou ímpar')
print('----------------------------------')

#1 Ler um número de 0 a 5, sortear para o usuário, e imprimir o resultado.

aposta = input('Você aposta em par ou ímpar?: ')

numero_do_usuario = int(input('Digite um número de 0 a 5: '))

sorteado = random.randint(0, 5)

print('Número sorteado:', sorteado)

resultado = numero_do_usuario + sorteado
print('A soma de', numero_do_usuario, '+', sorteado, 'é:', resultado)

if (aposta == 'par' and (resultado % 2) == 0) or (aposta == 'ímpar' and (resultado % 2) != 0):
    print('Você venceu!')

else:
    print('O programa venceu!')