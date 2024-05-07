from ConnectBD import conn

cursor = conn.cursor()

# Sub-Programas

def cadastrar():
  pass
 
def listar_Produtos():
  cursor.execute(f'SELECT * FROM cadastro.produto')
  result = cursor.fetchall()
  for row in result:
    nameProduct = row[1]
    CustoProduto = row[3]
    PercentCF = row[4]
    PercentCV = row[5]
    PercentIV = row[6]
    PercentML = row[7]
    
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
    
    print()
    print(f"{'-'*25} | {'-'*10} | {'-'*5}") 
    print (f"{'Descrição':^25} | {'Valor':^10} | {'%':^5}")
    print(f"{'-'*25} | {'-'*10} | {'-'*5}")
    
    print (f"{'A. Preço de Venda':<25} | {f'{PrecoVenda:.2f}':^10} | {f'{PercentPV}%':>5}")
    print (f"{'B. Custo de Aquisição':<25} | {f'{CustoProduto:.2f}':^10} | {f'{PercentCp:.0f}%':>5}")
    print (f"{'C. Receita Bruta (A-B)':<25} | {f'{ReceitaBruta:.2f}':^10} | {f'{PercentRb:.0f}%':>5}")
    print (f"{'D. Custo Fixo':<25} | {f'{Valor_CustoFixo:.2f}':^10} | {f'{PercentCF:.0f}%':>5}")
    print (f"{'E. Comissão de Vendas':<25} | {f'{Valor_ComisaoVendas:.2f}':^10} | {f'{PercentCV:.0f}%':>5}")
    print (f"{'F. Impostos':<25} | {f'{Valor_Imposto:.2f}':^10} | {f'{PercentIV:.0f}%':>5}")
    print (f"{'G. Outros custos (D+E+F)':<25} | {f'{OutrosCustos:.2f}':^10} | {f'{PercentOutrosCustos:.0f}%':>5}")
    print (f"{'H. Rentabilidade (C-G)':<25} | {f'{rent:.2f}':^10} | {f'{PercentML:.0f}%':>5}")
    
    print ("CLASSIFICAÇÃO DE LUCRO: ") 
    if MargemLucro>20:
        print(f'O lucro do {nameProduct} foi \033[34mAlto!\033[0m\n') #azul
    elif MargemLucro >10 and MargemLucro<=20:
        print(f'O lucro do {nameProduct} foi \033[32mMédio!\033[0m\n') #verde
    elif MargemLucro >0 and MargemLucro<=10:
        print(f'O lucro do {nameProduct} foi \033[33mBaixo!\033[0m\n') #amarelo
    elif MargemLucro == 0:
        print(f'O lucro do {nameProduct} foi Equilibrado!\n')
    else:
        print(f'O lucro do {nameProduct} foi \033[31mPrejuízo!\033[0m\n') #vermelho
    print ()
 
def atualizar():
  pass

def delete():
  pass 

 
# Menu do Programa
done = False
while not done:
  print('1. Cadastrar um Produto')
  print('2. Atualizar um Produto.')
  print('3. Deletar um Produto.')
  print('4. Listar Todos os Produtos.')
  print('5. Sair.')
  option = input('> ')
  
  if option == '1':
    print('Opcao nao implementada')
    cadastrar()    
    
  elif option == '2':
    print('Opcao nao implementada')
    atualizar()
    
  elif option == '3':
    print('Opcao nao implementada')
    delete()
    
  elif option == '4':
    print('Opcao nao implementada')
    listar_Produtos()
    
  elif option == '5':
    print('Saindo do programa...')
    break
   
  else:
    print('Digite uma opcao válida')
