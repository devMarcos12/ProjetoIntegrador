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
   print()
   id_produto = 0
   while True:
      try:
         id_produto = int(input("Digite o código do produto que deseja atualizar: "))

         if id_produto > 0:
            break
         else:
            print("Valor inválido! Digite números maiores que zero\n")
      except ValueError:
         print("Valor inválido! Digite somente números\n")

   cursor.execute(f"SELECT codTenis FROM cadastro.produto WHERE codTenis = {id_produto} LIMIT 1")
   retorno = cursor.fetchone() #Tenta recuperar o valor da primeira linha retornada

   if retorno is None:
      print("Desculpe, não foi encontrado nenhum produto cadastrado com o código informado\n")
   else:
      print("Produto Encontrado!")
      print("Dados do produto:")
      print()
      cursor.execute(f"SELECT nome, descricao, custoProduto, custoFixo, comissaoVendas, imposto, margemLucro FROM cadastro.produto WHERE codTenis = {id_produto}")
      retorno = cursor.fetchall()
      for row in retorno:
         print(f"Nome: {row[0]}")
         print(f"Descrição: {row[1]}")
         print(f"Custo do Produto: {row[2]}")
         print(f"Custo Fixo: {row[3]}")
         print(f"Valor da Comissão: {row[4]}")
         print(f"Valor do Imposto: {row[5]}")
         print(f"Margem de Lucro: {row[6]}")
      print()
      print("Selecione o campo que deseja atualizar")
      print()
      while True:
         print("1. Nome")
         print("2. Descrição")
         print("3. Custo do Produto")
         print("4. Custo Fixo")
         print("5. Valor da Comissão")
         print("6. Valor do Imposto")
         print("7. Margem de Lucro")
         print("8. Sair")
         print()

         opcao = 0
         while True:
            try:
               opcao = int(input("Informe a opção desejada: "))

               if opcao > 0 and opcao <= 8:
                  break
               elif opcao <= 0 or opcao > 8:
                  print("Opcão inválida! Informe somente números de 1 a 8\n")  
            except ValueError:
               print("Opçao inválida! Digite somente números\n")
         print()
         if opcao == 1:
            pass
         if opcao == 2:
            pass
         if opcao == 3:
            pass
         if opcao == 4:
            pass
         if opcao == 5:
            pass
         if opcao == 6:
            pass
         if opcao == 7:
           pass
         if opcao == 8:
            break
        

def delete():
    #   codigo_valido = False
    # while not codigo_valido:
    #     try:
    #         codigo_produto = int(input('Digite o código do produto: '))
    #         if codigo_produto > 0:
    #           codigo_valido = True
    #         else:
    #            print('Valor inválido! O código do produto deve ser maior que zero\n')
    #     except ValueError:
    #         print('Valor inválido! Digite somente números\n')
    
    # cursor.execute(f'SELECT * FROM cadastro.produto WHERE codTenis = {codigo_produto}')
  pass 


