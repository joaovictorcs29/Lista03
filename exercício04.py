print('Exercício 4 - Criar um programa que verifica se um número inteiro é divisível por 3') 
print('-----------------------------------------------------------------------------------')

# '%' serve pra calcular o resto da divisão

#1 Verificar se um número inteiro é divisível por 3

nmro = int(input('Digite um número inteiro: '))

if ((nmro % 3) == 0):
    print('O número é divisível por 3')

else:
    print('Seu número não é divisível por 3')
