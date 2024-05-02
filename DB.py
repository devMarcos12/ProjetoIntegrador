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
      
  elif option == 3:
    print('Opcao nao implementada')
  elif option == 4:
    print('Opcao nao implementada')
  else:
    done = True
