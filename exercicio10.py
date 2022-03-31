import random
 
print('Exercício 10 - Programa que simula dados de 4, 6, 8, 10, 12 ou 16 faces')
print('-----------------------------------------------------------------------')

#Ler os  dados de 4, 6, 8, 10, 12 ou 16 lados
#1 Apresentar menu de escolha 
print('1)Dado de 4 faces')
print('2)Dado de 6 faces')
print('3)Dado de 8 faces')
print('4)Dado de 10 faces')
print('5)Dado de 12 faces')
print('6)Dado de 16 faces')

escolhido = int(input('Digite o tipo de dado a ser sorteado: '))

print('-------------------------------------------------------')

if escolhido == 1:
   print('Número sorteado é:',  random.randint (1, 4))

elif escolhido == 2:
     print('Número sortedo é:',random.randint (1, 6))

elif escolhido == 3:
     print('Número sortedo é:',random.randint (1, 8))

elif escolhido == 4:
     print('Número sortedo é:', random.randint (1, 10))

elif escolhido == 5:
     print('Número sortedo é:',random.randint (1, 12))

elif escolhido == 6: 
     print('Número sortedo é:',random.randint(1, 16))
   
else:  
      print('Erro. Coloque uma opção válida: ')
