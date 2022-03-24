print('Exercício 5 - Algoritmo para receber um número qualquer do usuário e informar na tela se é par ou se é ímpar')
print('------------------------------------------------------------------------------------------------------------')

#1 Ler um número e informar se é par ou ímpar

n = int(input('Digite um número: '))

if  ((n % 2) == 0):
    print('Seu número é par')

else:
    print('Seu número é impar')