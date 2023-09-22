class Tarefa:
    def __init__(self, descricao, feita=False):
        self.descricao = descricao
        self.feita = feita
        self.proxima = None
