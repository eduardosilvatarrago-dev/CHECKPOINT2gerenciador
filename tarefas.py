import json, os 

lista_tarefas = []

def adicionar_tarefa(descricao):
   nova_tarefa = {'descricao': descricao,
                 'concluido': False}
   lista_tarefas.append(nova_tarefa)
   print('tarefa adicionada com sucesso')

def salvar_dados():
    with open('tarefas.json', 'w') as arquivo:
        json.dump(lista_tarefas, arquivo, indent=4)
    print('dados salvos com sucesso')

def carregar_dados():
    global lista_tarefas
    try:
      with open('tarefas.json', 'r') as arquivo:
        lista_tarefas = json.load(arquivo)
      print('dados carregados com sucesso')
    except FileNotFoundError:
      print('arquivo nao encontrado')
      lista_tarefas = []



def listar_tarefas():
  print('lista de tarefas')
  for i, tarefa in enumerate(lista_tarefas):
    status = '[x]' if tarefa['concluido'] else '[]'
    print(f'{i} - {status} {tarefa["descricao"]}')
  print('______________________\n')

def concluir_tarefa(indice):
  try:
    lista_tarefas[indice]['concluido'] = True
    print('Tarefa concluida com sucesso')
  except IndexError:
    print('indice invalido')
  print('______________________\n')


def limpar_tela():
   os.system('cls' if os.name == 'nt' else 'clear')
