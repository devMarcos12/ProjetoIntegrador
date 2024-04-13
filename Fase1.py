import os

def clear():
  os.system('cls')

colors = {
  'limpa': '\033[m',
  'azul': '\03330;44',
  'verde': '\0337;32',
  'amarelo': '\0337;33',
  'branco': '\0337;30',
  'vermelho': '\03331;40'
}

name = input('Digite o nome do produto: ')
cod = int(input('Digite o código do Produto: '))
CustoProduto = float(input('Qual o custo do Produto (CA)? '))
PercentCF = int(input('Qual o custo Fixo/Administrativo(CF)? '))
PecentCV = int(input('Qual a Commissão de Vendas (CV)? '))
PercentIV = int(input('Qual o Imposto (IV)? '))
PercentML = int(input('Qual a Margem de lucro(ML)? '))
PrecoVenda = CustoProduto / (1-((PercentCF+PecentCV+PercentIV+PercentML)/(100)))

# Calculando a Receita Bruta do Produto
ReceitaBruta = PrecoVenda - CustoProduto 

# Calculando quantos reais as procentagens estão gerando em cima do Preço de Venda
CustoFixo = 15 * PrecoVenda / 100
ComissaoVendas = 5 * PrecoVenda / 100
Imposto = 12 * PrecoVenda / 100


# Cálculo de Outros Custos
OutrosCustos = CustoFixo + ComissaoVendas + Imposto 

# Cálculo a Rentabilidade
rent = ReceitaBruta - OutrosCustos 

# Cálculo das Procentagem
PercentCp = CustoProduto * 100 / PrecoVenda

PercentRb = ReceitaBruta * 100 / PrecoVenda

PercentOc = OutrosCustos * 100 / PrecoVenda

PercentRent = rent * 100 / PrecoVenda

def exibirTabela():
  print('Descrição           /    Valor       /   %')
  print(f'Preço de Venda:     / {PrecoVenda}   /  100%')
  print(f'Custo de Aquisição: / {CustoProduto} /  {PercentCp}%')
  print(f'Receita Bruta:      / {ReceitaBruta} /  {PercentRb}%')
  print(f'Custo Fixo:         / {CustoFixo}    /  {PercentCF}%')
  print(f'Comissão de Venda:  / {ComissaoVendas}    /  {PecentCV}%')
  print(f'Impostos:           / {Imposto}   /  {PercentIV}%')
  print(f'Outros Custos:      / {OutrosCustos} /  {PercentOc}%')
  print(f'Rentabilidade:      / {rent}         /  {PercentRent}% \n\n')
  
def lucroRent():
  if PercentRent > 20:
    print(f'\033[30;44mO lucro do {name} foi Alto!')
  elif PercentRent <= 20:
    print(f'O lucro do {name} foi Médio!')
  elif PercentRent <= 10:
    print(f'\033[7;32mO lucro do {name} foi Baixo!')
  elif PercentRent == 0:
    print(f'O lucro do {name} foi Equilibrado!')
  elif PercentRent < 0:
    print(f'O lucro do {name} foi Prejuízo!')
    
  
done = False

while not done:
  try:
    print('Qual opção deseja?')
    print('1 - Descrição, Valor e Porcentagem.')
    print('2 -  Qual a classificação do Lucro que o produto está.')
    print('3 - Sair.')
    choice = input('> ')
    clear()

    if choice == '1':
      clear()
      exibirTabela()
    elif choice == '2':
      clear()
      lucroRent()
    elif choice == '3':
      done = True
    else:
      clear()
      print('Digite uma opção entre 1 e 3')
  except ValueError:
    clear()
    print('Somente números de 1 a 3')