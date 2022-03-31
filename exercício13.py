from bdb import GENERATOR_AND_COROUTINE_FLAGS


print('Exercício 13 - Um programa que leia a nota do Grau A e do Grau B do aluno e calcule a média final conforme as regras da Unisinos')
print('--------------------------------------------------------------------------------------------------------------------------------')

#1) Ler a nota do grau A e B do aluno
grau_a = float(input('Digite a nota do grau a: '))
grau_b = float(input('Digite a nota do grau b: '))
#2) Calcular média final sem recuperação 
grau_final = (grau_a * 0.33) + (grau_b * 0.67)
print('Média final: ', grau_final)

if grau_final >= 6:
   print('Aprovado')

elif grau_final < 6:
     print('Recuperação')
#3) ler nota do grau C
     grau_c = float(input('Digite a nota do grau C: '))

#4) Perguntar qual grau quer substituir.

print('Qual grau substituir pelo grau c?')  
print('1) Grau a') 
print('2) Grau b')
grau_substituido = int(input('Digite opção: '))

#5) Recalcular

if grau_substituido == 1:
   notal_final_grau_c = (grau_c * 0.33) + (grau_b * 0.67)

   if notal_final_grau_c >= 6: 
       print('Aprovado', notal_final_grau_c)
   else:
       print('Reprovado')  

elif grau_substituido == 2:
    notal_final_grau_c = (grau_a * 0.33) + (grau_c * 0.67)
    
    if notal_final_grau_c >= 6: 
        print('Aprovado', notal_final_grau_c)
    else:
        print('Reprovado')  
