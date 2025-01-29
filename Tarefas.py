class Tarefa:
    def __init__(self, data, tarefa):
        self._data = data
        self._tarefa = tarefa
        self._concluido = False


    def alterar_conclusao(self):
        self._concluido = not self._concluido