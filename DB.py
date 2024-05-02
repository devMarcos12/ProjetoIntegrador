from ConnectBD import conn

cursor = conn.cursor()
 
done = False
while not done:
  print('1 - Create')
  print('2 - Read')
  print('3 - Update')
  print('4 - Delete')
  option = input('> ')
  
  if option == '1':
    print('Opcao nao implementada')    
  elif option == '2':
    codigo_valido = False
    while not codigo_valido:
        try:
            codigo_produto = int(input('Digite o código do produto: '))
            if codigo_produto > 0:
              codigo_valido = True
            else:
               print('Valor inválido! O código do produto deve ser maior que zero\n')
        except ValueError:
            print('Valor inválido! Digite somente números\n')
    
    cursor.execute(f'SELECT * FROM cadastro.produto WHERE codTenis = {codigo_produto}')
    result = cursor.fetchall()
    for row in result:
      nameProduct = row[1]
      CustoProduto = row[3]
      PercentCF = row[4]
      PercentCV = row[5]
      PercentIV = row[6]
      PercentML = row[7]
      
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
      
  elif option == 3:
    print('Opcao nao implementada')
  elif option == 4:
    print('Opcao nao implementada')
  else:
    done = True
