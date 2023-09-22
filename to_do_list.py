from tarefas import Tarefa

class ToDoList:
    def __init__(self):
        self.inicio = None

    def inserir_tarefa(self, descricao):
        nova_tarefa = Tarefa(descricao)
        if not self.inicio:
            self.inicio = nova_tarefa
        else:
            atual = self.inicio
            while atual.proxima:
                atual = atual.proxima
            atual.proxima = nova_tarefa

    def listar_tarefas(self):
        if not self.inicio:
            print("A lista de tarefas está vazia.")
        else:
            atual = self.inicio
            index = 1
            while atual:
                status = "Feita" if atual.feita else "Pendente"
                print(f"{index}. [{status}] {atual.descricao}")
                atual = atual.proxima
                index += 1

    def marcar_como_feita(self, numero):
        atual = self.inicio
        index = 1
        while atual:
            if index == numero:
                atual.feita = True
                return
            atual = atual.proxima
            index += 1

    def desmarcar_como_feita(self, numero):
        atual = self.inicio
        index = 1
        while atual:
            if index == numero:
                atual.feita = False
                return
            atual = atual.proxima
            index += 1

    def remover_tarefa(self, numero):
        if not self.inicio:
            print("A lista de tarefas está vazia.")
            return

        if numero == 1:
            self.inicio = self.inicio.proxima
        else:
            atual = self.inicio
            index = 1
            while atual:
                if index == numero - 1:
                    atual.proxima = atual.proxima.proxima if atual.proxima else None
                    return
                atual = atual.proxima
                index += 1

    def alterar_tarefa(self, numero, nova_descricao):
        atual = self.inicio
        index = 1
        while atual:
            if index == numero:
                atual.descricao = nova_descricao
                return
            atual = atual.proxima
            index += 1
