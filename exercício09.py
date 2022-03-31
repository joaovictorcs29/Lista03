import locale

print('Exercício 9 - Conversor de câmbio de reais/dólar/euro')
print('-----------------------------------------------------')

#1) Informar a cotação

dolar = float(input('Digite a cotação do dólar: ') or 4.7782007)
euro = float(input('Digite a cotação do euro: ') or 5.2479003)
real = 1

#2) Apresentar menu de escolha
print('-------------------------------')
print('1) Converter de Real para Euro')
print('2) Converter de Real para Dólar')
print('3) Converter de Euro para Dólar')
print('4) Converter de Euro para Real')
print('5) Converter de Dólar para Euro')
print('6) Converter de Dólar para Real')
print('-------------------------------')

#3 Fazer a conversão
def get_opcao(num_opcao):
    if num_opcao < 1 or num_opcao > 6:
        print('Opção inválida')
        exit
    else:
        valor = float(input('Digite valor a ser convertido: '))
        match num_opcao:
            case 1: # Real -> Euro
                moeda_conversao = 'Real -> Euro'
                taxa_conversao =  real / euro
                locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')
            case 2: # Real -> Dólar
                moeda_conversao = 'Real -> Dólar'
                taxa_conversao = real / dolar
                locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
            case 3: # Euro -> Dólar
                moeda_conversao = 'Euro -> Dólar'
                taxa_conversao = euro / dolar
                locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
            case 4: # Euro -> Real
                moeda_conversao = 'Euro -> Real'
                taxa_conversao = euro / real
                locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
            case 5: # Dólar -> Euro
                moeda_conversao = 'Dólar -> Euro'
                taxa_conversao = dolar/ euro
                locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')
            case 6: # Dólar -> Real
                moeda_conversao = 'Dólar -> Real'
                taxa_conversao = dolar / real
                locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        valor_conversao = valor * taxa_conversao
        print('-------------------------------')
        print('A taxa de conversão de', moeda_conversao, 'é:', round(taxa_conversao, 7))
        print('O valor na moeda destino é:', locale.currency(valor_conversao, grouping=True))

get_opcao(int(input('Digite a opção de menu desejada: ')))
