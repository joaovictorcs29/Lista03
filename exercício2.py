print('Exercício 2 - Ler os valores A, B, C e imprimir na tela se a soma de A + B é menor que A + C')
print('--------------------------------------------------------------------------------------------')

#1 Ler os valores e efetuar a soma 
varA = input('Digite o valor de A: ')
varB = input('Digite o valor de B: ')
varC = input('Digite o valor de C: ')

if (varA + varB) < (varA + varC):
    print('A soma de A + B é menor que A + C')
else:
    print ('A soma de A + B é maior ou igual a A + C')
    