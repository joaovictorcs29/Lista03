print('Exercício 1 - Ler dois números e efetuar uma divisão, mas somente se o divisor for diferente de zero; quando ocorrer isso, é mostrada uma mensagem de erro')
print('----------------------------------------------------------------------------------------------------------------------------------------------------------')

#1 Ler dois números e efetuar divisão se for diferente de 0
varA = float(input('Digite o primeiro número: '))
varB = float(input('Digite o segundo número: '))

if (varB == 0):
    print('O número não pode ser dividido')
else:
    divisao = varA / varB
    print ('Sua divisáo é:', "{:.1f}".format(divisao).replace('.',','))
