import os

def clear():
  os.system('cls')

try: 
  nameProduct = input('Digite o nome do produto: ')
  cod = int(input('Digite o código do Produto: '))
  if cod <= 0:
    print('Código inválido, o código deve ser maior do que 0!')
  else:
    CustoProduto = float(input('Qual o custo do Produto (porcentagem)? '))
    if CustoProduto <= 0:
      print('A porcentagem do Custo do Produto deve ser maior do que 0!')
    else:
      PercentCF = int(input('Qual o custo Fixo/Administrativo (porcentagem)? '))
      if PercentCF <= 0:
        print('A porcentagem do Custo Fixo/Administrativo deve ser maior do que 0!')
      else:
        PercentCV = int(input('Qual a Commissão de Vendas (CV)? '))
        if PercentCV <= 0:
          print('A porcentagem da Comissão de Vendas deve ser maior do que 0!')
        else:
          PercentIV = int(input('Qual o Imposto (IV)? '))
          if PercentIV <= 0:
            print('A porcentagem do Imposto deve ser maior do que 0!')
          else: 
            PercentML = int(input('Qual a Margem de lucro(ML)? '))
            if PercentML <= 0:
              print('A porcentagem da Margem de Lucro deve ser maior do que 0!')
except ValueError:
  print('O valor deve ser maior do que 0')

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
  print('-'*50)
  print('Descrição           /    Valor       /   %')
  print(f'A. Preço de Venda:     / {PrecoVenda:.2f}   /  {PercentPV}')
  print(f'B. Custo de Aquisição: / {CustoProduto:.2f} /  {PercentCp}%')
  print(f'C. Receita Bruta:      / {ReceitaBruta:.2f} /  {PercentRb}%')
  print(f'D. Custo Fixo:         / {Valor_CustoFixo:.2f}    /  {PercentCF}%')
  print(f'E. Comissão de Venda:  / {Valor_ComisaoVendas:.2f}    /  {PercentCV}%')
  print(f'F. Impostos:           / {Valor_Imposto:.2f}   /  {PercentIV}%')
  print(f'G. Outros Custos:      / {OutrosCustos:.2f} /  {PercentOutrosCustos}%')
  print(f'H. Rentabilidade:      / {rent:.2f}         /  {PercentML}% \n')
  print('-'*50)
  
def lucroRent():
  if MargemLucro > 20:
    print(f'O lucro do {nameProduct} foi \33[42mAlto!\33[m\n')
  elif MargemLucro > 10 and MargemLucro <= 20:
    print(f'O lucro do {nameProduct} foi \33[43mMédio!\33[m\n')
  elif MargemLucro > 0 and  MargemLucro <= 10:
    print(f'O lucro do {nameProduct} foi \33[44mBaixo!\33[m\n')
  elif MargemLucro == 0:
    print(f'O lucro do {nameProduct} foi \33[45mEquilibrado!\33[m\n')
  else:
    print(f'O lucro do {nameProduct} foi \33[41mPrejuízo!\33[m\n')
    
  
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