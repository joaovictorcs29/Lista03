import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

print('Exercício 8 - Entrar com o valor do produto e imprimir na tela o valor de venda')
print('-------------------------------------------------------------------------------')

#1) Ler valor de compra e descontos

compra = float(input('Valor do produto (R$): '))
desconto1 = 0.45
desconto2 = 0.35 
desconto3 = 0.25

#2) Verificar lucro sobre os produtos

if compra <= 20:
   desconto = desconto1

elif compra <= 50:
    desconto = desconto2

else: 
    compra > 50
    desconto = desconto3

#3) Calcular o valor com lucro
lucro = compra * desconto
valor_com_lucro = compra + lucro

#4) Formatar a resposta para o comerciante (usuário)
desconto_formatado = str(int(desconto * 100))
valor_com_lucro_formatado_em_reais = locale.currency(valor_com_lucro, grouping=True, symbol='R$')

print('Valor de venda com ' + desconto_formatado + '% de lucro:', valor_com_lucro_formatado_em_reais)
