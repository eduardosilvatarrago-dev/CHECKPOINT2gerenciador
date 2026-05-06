from tarefas import adicionar_tarefa, listar_tarefas, concluir_tarefa, salvar_dados, carregar_dados, limpar_tela

carregar_dados() 

while True:
    limpar_tela()
    print('----gerenciador de tarefas----')
    print('\n 1-adicionar tarefa')
    print('2-listar tarefas')
    print('3-concluir tarefas')
    print('4-salvar e sair')
    
    opcao = input('Digite a opcao desejada: ')

    if opcao == '1':
        limpar_tela()
        descricao = input('digite a descricao da tarefa: ')
        adicionar_tarefa(descricao)
        
    elif opcao == '2':
        limpar_tela()
        listar_tarefas()
        
    elif opcao == '3':
        limpar_tela()
        try:
            num = int(input('digite o numero da tarefa a ser concluida: '))
            concluir_tarefa(num)
        except ValueError:
            print('numero invalido')
            
    elif opcao == '4':
        limpar_tela()
        salvar_dados()
        print('saindo do programa')
        break
        
    else:
        limpar_tela()
        print('opcao invalida')