from ConnectBD import create_connection, create_cursor, execute_query, fetch_query_results

# Sub-Programas
def cadastrar():

   conn = create_connection('localhost', 'root', '1234', 'Cadastro')
   cursor = create_cursor(connection=conn)

   print()

   def verificar_numero(entrada):
       try:
           float(entrada)
           return True
       except ValueError:
           return False

   def verificar_positivo(entrada):
       return entrada >= 0
   
   nomeTenis = input("Digite o nome do Tênis: ")
   while not nomeTenis.strip():
       print("Por favor, insira um nome válido para o Tênis.")
       nomeTenis = input("Digite o nome do Tênis: ")

   # Solicitar e verificar a descrição
   descricao = input("Digite a descrição: ")
   while not descricao.strip(): 
       print("Por favor, insira uma descrição válida.")
       descricao = input("Digite a descrição: ")

   custoProduto = input("Digite o custo do produto: ")
   while not (verificar_numero(custoProduto) and verificar_positivo(float(custoProduto))):
       print("Por favor, insira um valor numérico positivo para o custo do produto.")
       custoProduto = input("Digite o custo do produto: ")

   custoFixo = input("Digite o custo fixo: ")
   while not (verificar_numero(custoFixo) and verificar_positivo(float(custoFixo))):
       print("Por favor, insira um valor numérico positivo para o custo fixo.")
       custoFixo = input("Digite o custo fixo: ")

   # Solicitar e verificar a comissão de vendas
   comissaoVendas = input("Digite a comissão de vendas: ")
   while not (verificar_numero(comissaoVendas) and verificar_positivo(float(comissaoVendas))):
       print("Por favor, insira um valor numérico positivo para a comissão de vendas.")
       comissaoVendas = input("Digite a comissão de vendas: ")

   # Solicitar e verificar o imposto
   imposto = input("Digite o imposto: ")
   while not (verificar_numero(imposto) and verificar_positivo(float(imposto))):
       print("Por favor, insira um valor numérico positivo para o imposto.")
       imposto = input("Digite o imposto: ")

   # Solicitar e verificar a margem de lucro
   margemLucro = input("Digite a margem de lucro: ")
   while not (verificar_numero(margemLucro) and verificar_positivo(float(margemLucro))):
       print("Por favor, insira um valor numérico positivo para a margem de lucro.")
       margemLucro = input("Digite a margem de lucro: ")

   sql = "INSERT INTO cadastro.produto (nome, descricao, custoProduto, custoFixo, comissaoVendas, imposto, margemLucro) VALUES (%s, %s, %s, %s, %s, %s, %s)"
   val = (nomeTenis, descricao, custoProduto, custoFixo, comissaoVendas, imposto, margemLucro)
   cursor.execute(sql, val)
   
   conn.commit()
   print()
   print("DADO INSERIDO COM SUCESSO!")
   print()
   cursor.close()
   conn.close()
      
 
def listar_Produtos():
   conn = create_connection('localhost', 'root', '1234', 'Cadastro')
   cursor = create_cursor(connection=conn)
   cursor.execute(f'SELECT * FROM cadastro.produto')
   result = cursor.fetchall()
   for row in result:
      nameProduct = row[1]
      CustoProduto = row[3]
      PercentCF = row[4]
      PercentCV = row[5]
      PercentIV = row[6]
      PercentML = row[7]
     
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
      if PercentML>20:
         print(f'O lucro do {nameProduct} foi \033[34mAlto!\033[0m\n') #azul
      elif PercentML >10 and PercentML<=20:
         print(f'O lucro do {nameProduct} foi \033[32mMédio!\033[0m\n') #verde
      elif PercentML >0 and PercentML<=10:
         print(f'O lucro do {nameProduct} foi \033[33mBaixo!\033[0m\n') #amarelo
      elif PercentML == 0:
         print(f'O lucro do {nameProduct} foi Equilibrado!\n')
      else:
         print(f'O lucro do {nameProduct} foi \033[31mPrejuízo!\033[0m\n') #vermelho
      print()
 
def atualizar():
   conn = create_connection('localhost', 'root', '1234', 'Cadastro')
   cursor = create_cursor(connection=conn)
   print()
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
      cursor.execute(f"SELECT * FROM cadastro.produto WHERE codTenis = {id_produto}")
      retorno = cursor.fetchall()
      for row in retorno:
         print(f"Nome: {row[1]}")
         print(f"Descrição: {row[2]}")
         print(f"Custo do Produto: {row[3]}")
         print(f"Custo Fixo: {row[4]}")
         print(f"Valor da Comissão: {row[5]}")
         print(f"Valor do Imposto: {row[6]}")
         print(f"Margem de Lucro: {row[7]}")
      print()
      while True:
         print("Selecione o campo que deseja atualizar")
         print("1. Nome")
         print("2. Descrição")
         print("3. Custo do Produto")
         print("4. Custo Fixo")
         print("5. Valor da Comissão")
         print("6. Valor do Imposto")
         print("7. Margem de Lucro")
         print("8. Sair")
         print()

         while True:
            conn = create_connection('localhost', 'root', '1234', 'Cadastro')
            cursor = create_cursor(connection=conn)
            try:
               opcao = int(input("Informe a opção desejada: "))

               if opcao > 0 and opcao <= 8:
                  break
               elif opcao <= 0 or opcao > 8:
                  print("Opcão inválida! Informe somente números de 1 a 8\n")  
            except ValueError:
               print("Opçao inválida! Digite somente números\n")
         print()
         
         if opcao == 1: # Altera o Nome
            try:
               newName = input('Digite o novo nome do produto: ')
            except ValueError:
               print('Apenas letras')
            
            cursor.execute(f'UPDATE cadastro.produto SET nome = "{newName}" WHERE codTenis = {id_produto}')
            conn.commit()
            print('\nNome atualizado com sucesso!\n')
            cursor.close()
            conn.close()
            
         if opcao == 2: # Altera o Descricao
            try:
               newDesc = input('Digite a nova descicao do produto: ')
            except ValueError:
               print('Apenas letras')
                    
            cursor.execute(f'UPDATE cadastro.produto SET descricao = "{newDesc}" WHERE codTenis = {id_produto}')
            conn.commit()
            print('\nDescricao atualizado com sucesso!\n')
            # print(cursor.rowcount, ' registros atualizados')
            cursor.close()
            conn.close()
         if opcao == 3:
            # Obtendo o novo valor do Custo do Produto
            try:
               while True:
                  newPercentCP = float(input('Qual o novo custo do produto? '))
                  if newPercentCP <= 0:
                     print('Só aceitamos números positivos.')
                  else:
                     break
            except ValueError:
               print('Digite um número inteiro e positivo')
            # Alterando para o novo valor
            
            cursor.execute(f'UPDATE cadastro.produto SET custoProduto = {newPercentCP} WHERE codTenis = {id_produto}')
            conn.commit()
            print('\nCusto do Produto atualizado com sucesso!\n')
            cursor.close()
            conn.close()
                           
         if opcao == 4:
            # Obtendo o novo valor do Custo Fixo
            try:
               while True:
                  newPercentCF = float(input('Qual o novo custo fixo: '))
                  if newPercentCF <= 0:
                     print('Só aceitamos números positivos.')
                  else:
                     break
            except ValueError:
               print('Digite um número inteiro e positivo')
            # Alterando para o novo valor
            
            cursor.execute(f'UPDATE cadastro.produto SET custoFixo = {newPercentCF} WHERE codTenis = {id_produto}')
            conn.commit()
            print('\nCusto Fixo atualizado com sucesso!\n')
            cursor.close()
            conn.close()
                
         if opcao == 5:
            # Obtendo o novo valor da Comissao de Vendas
            try:
               while True:
                  newPercentCV = float(input('Qual o novo valor da Comissao de Vendas: '))
                  if newPercentCV <= 0:
                     print('Só aceitamos números positivos.')
                  else:
                     break
            except ValueError:
               print('Digite um número inteiro e positivo')
            # Alterando para o novo valor
            
            cursor.execute(f'UPDATE cadastro.produto SET comissaoVendas = {newPercentCV} WHERE codTenis = {id_produto}')
            conn.commit()
            print('\nComissao de Vendas atualizada com sucesso!\n')
            cursor.close()
            conn.close()
                
         if opcao == 6:
            # Obtendo o novo valor do Imposto
            try:
               while True:
                  newPercentIV= float(input('Qual o novo valor do Imposto: '))
                  if newPercentIV <= 0:
                     print('Só aceitamos números positivos.')
                  else:
                     break
            except ValueError:
               print('Digite um número inteiro e positivo')
            # Alterando para o novo valor
            
            cursor.execute(f'UPDATE cadastro.produto SET imposto = {newPercentIV} WHERE codTenis = {id_produto}')
            conn.commit()
            print('\nImposto atualizado com sucesso!\n')
            cursor.close()
            conn.close()
         if opcao == 7: # Margem de Lucro
            # Obtendo a nova Margem de Lucro
            try:
               while True:
                  newPercentML = float(input('Qual a nova Margem de Lucro: '))
                  if newPercentML <= 0:
                     print('Só aceitamos números positivos.')
                  else:
                     break
            except ValueError:
               print('Digite um número inteiro e positivo')
            # Alterando para o novo valor
            
            cursor.execute(f'UPDATE cadastro.produto SET margemLucro = {newPercentML} WHERE codTenis = {id_produto}')
            conn.commit()
            print('\nMargem de Lucro atualizada com sucesso!\n')
            cursor.close()
            conn.close()
         if opcao == 8:
            break

def excluir_tenis(conn, codTenis):
   cursor = create_cursor(connection=conn)
    
   cursor = conn.cursor()
   query = "DELETE FROM cadastro.produto WHERE codTenis = %s"
   cursor.execute(query, (codTenis,))
   conn.commit()
   print(f"Tênis com código {codTenis} foi excluído.\n")
   cursor.close()

def delete():
   conn = create_connection('localhost', 'root', '1234', 'Cadastro')

   while True:
      try:
         codTenis = int(input("Digite o código do tênis a ser excluído: "))
         if codTenis > 0:
            excluir_tenis(conn, codTenis)
            break
         else:
            print("Por favor, digite um número natural maior que zero.")
      except ValueError:
            print("Entrada inválida. Por favor, digite um número natural maior que zero.")     
      conn.close()

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