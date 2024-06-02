from CRUD import listar_Produtos, delete, atualizar, cadastrar

done = False
while not done:
  print('1. Cadastrar um Produto')
  print('2. Atualizar um Produto.')
  print('3. Deletar um Produto.')
  print('4. Listar Todos os Produtos.')
  print('5. Sair.')
  option = input('> ')
  
  if option == '1':
    cadastrar()    
    
  elif option == '2':
    atualizar()
    
  elif option == '3':
    delete()
    
  elif option == '4':
    listar_Produtos()
    
  elif option == '5':
    print('Saindo do programa...')
    break
   
  else:
    print('Digite uma opcao válida.')
