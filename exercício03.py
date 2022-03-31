print('Exercício 3 - Encontrar o dobro de um número caso ele seja positivo e o seu triplo caso seja negativo, e imprimir o resultado')
print('-----------------------------------------------------------------------------------------------------------------------------')

#1 Encontrar o dobro de um número caso ele seja positivo e o seu triplo caso seja negativo
nmr1 = int(input('Digite um número inteiro: '))

if (nmr1 > 0):
   resultado = nmr1 * 2
   print('O seu número é positivo, então o dobro é:', resultado)

elif (nmr1 < 0):
    resultado = nmr1 * 3
    print('O seu número é negativo, então o triplo é:', resultado)

else:
    print('Seu número é zero')
    
