from ensurepip import bootstrap


print('Exercício 7 - Um programa que calcula o desconto previdenciário de um funcionário')
print('---------------------------------------------------------------------------------')

#1 Calcular o desconto em 11%, caso exceda o valor descontar em 318,20

salario = float(input('Seu salário: '))
desconto = 0.11 
valor_maximo_desconto = 318.20
desconto_proporcional = salario * 0.11

if (desconto_proporcional <= 318.20):
    print('Seu salário foi descontado em:', desconto_proporcional)

else:
    print('Seu salário foi descontado em: ', valor_maximo_desconto)

    
