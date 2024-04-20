import os

def clear():
  os.system('cls')

name = input('Digite o nome do produto: ')
cod = int(input('Digite o código do Produto: '))
CustoProduto = float(input('Qual o custo do Produto (CA)? '))
PercentCF = int(input('Qual o custo Fixo/Administrativo(CF)? '))
PercentCV = int(input('Qual a Commissão de Vendas (CV)? '))
PercentIV = int(input('Qual o Imposto (IV)? '))
PercentML = int(input('Qual a Margem de lucro(ML)? '))


# Calculando quantos reais as procentagens estão gerando em cima do Preço de Venda
CustoFixo = (CustoProduto/100) * PercentCF
ComissaoVendas = (CustoProduto/100) * PercentCV
Imposto = (CustoProduto/100) * PercentIV
MargemLucro = (CustoProduto/100) * PercentML 

# Cálculo Preço de Venda
PrecoVenda = CustoProduto / (1-((PercentCF+PercentCV+PercentIV+PercentML)/(100)))
PercentPV = 100

# Cálculo das Procentagem
PercentCp = PercentPV - PercentCF - PercentCV - PercentIV - PercentML

# Cálculo Receita Bruta
ReceitaBruta = PrecoVenda - CustoProduto
PercentRb = PercentPV - PercentCp

#transformando as porcentagens lidas nos respectivos valores
Valor_CustoFixo = (PrecoVenda / 100 ) * PercentCF
Valor_ComisaoVendas = (PrecoVenda / 100) * PercentCV
Valor_Imposto = (PrecoVenda / 100) * PercentIV

# Cálculo de Outros Custos
OutrosCustos = Valor_CustoFixo + Valor_ComisaoVendas + Valor_Imposto
PercentOutrosCustos = PercentCF + PercentCV + PercentIV

# Cálculo Rentabilidade
rent = ReceitaBruta - OutrosCustos


def exibirTabela():
  print('Descrição           /    Valor       /   %')
  print(f'Preço de Venda:     / {PrecoVenda:.2f}   /  {PercentPV}')
  print(f'Custo de Aquisição: / {CustoProduto:.2f} /  {PercentCp}%')
  print(f'Receita Bruta:      / {ReceitaBruta:.2f} /  {PercentRb}%')
  print(f'Custo Fixo:         / {Valor_CustoFixo:.2f}    /  {PercentCF}%')
  print(f'Comissão de Venda:  / {Valor_ComisaoVendas:.2f}    /  {PercentCV}%')
  print(f'Impostos:           / {Valor_Imposto:.2f}   /  {PercentIV}%')
  print(f'Outros Custos:      / {OutrosCustos:.2f} /  {PercentOutrosCustos}%')
  print(f'Rentabilidade:      / {rent:.2f}         /  {PercentML}% \n\n')
  
def lucroRent():
  if MargemLucro > 20:
    print(f'O lucro do {name} foi Alto!')
  elif MargemLucro > 10 and MargemLucro <= 20:
    print(f'O lucro do {name} foi Médio!')
  elif MargemLucro > 0 and  MargemLucro <= 10:
    print(f'O lucro do {name} foi Baixo!')
  elif MargemLucro == 0:
    print(f'O lucro do {name} foi Equilibrado!')
  else:
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