from to_do_list import ToDoList
from tarefas import Tarefa

def menu():
    lista_tarefas = ToDoList()
    while True:
        escolha = input(
            """
            ===========================
                MENU - To do List
            ===========================
            1- Adicionar Tarefas
            2- Remover Tarefas
            3- Alterar Tarefas
            4- Marcar Tarefa como Feita
            5- Desmarcar tarefa como Feita
            6- Lista de Tarefas
            7 - SAIR
            escolha: """ # adicionei a opção 6 SAIR para conseguir dar um break no while.
        )
        if escolha == "1":
            descricao = input("Digite a descrição da tarefa: ")
            lista_tarefas.inserir_tarefa(descricao)
        elif escolha == "2":
            numero = int(input("Digite o número da tarefa a ser removida: "))
            lista_tarefas.remover_tarefa(numero)
        elif escolha == "3":
            numero = int(input("Digite o número da tarefa a ser alterada: "))
            nova_descricao = input("Digite a nova descrição: ")
            lista_tarefas.alterar_tarefa(numero, nova_descricao)
        elif escolha == "4":
            numero = int(input("Digite o número da tarefa a ser marcada como feita: "))
            lista_tarefas.marcar_como_feita(numero)
        elif escolha == "5":
            numero = int(input("Digite o número da tarefa a ser desmarcada como feita: "))
            lista_tarefas.desmarcar_como_feita(numero)
        elif escolha == "6":
            lista_tarefas.listar_tarefas()
        elif escolha == "7":
            break
        else:
            print("Escolha inválida, favor, selecionar uma opção do menu")
