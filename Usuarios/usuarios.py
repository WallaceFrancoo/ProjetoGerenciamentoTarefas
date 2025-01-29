from Tarefas import Tarefa

class Usuarios:
    usuarios = []

    def __init__(self,nome, departamento, senha):
        self._nome = nome
        self._departamento = departamento
        self._senha = senha
        self._tarefas = []
        Usuarios.usuarios.append(self)

    def __str__(self):
        return self._nome

    @classmethod
    def mostrar_usuarios(cls):
        for usuario in cls.usuarios:
            print(f'{usuario._nome} é do departamento {usuario.departamento} a senha dele é: {usuario._senha} tem as tarefas: {usuario.mostrar_tarefas}')

    @property
    def departamento(self):
        return 'Departamento de Tecnologia' if self._departamento == 'T.I' else 'Cadastrar departamento'

    def criar_tarefa(self, data, tarefa):
        tarefa = Tarefa(data, tarefa)
        self._tarefas.append(tarefa)

    @property
    def mostrar_tarefas(self):
        if not self._tarefas:
            return "\n" + "Sem tarefas atribuídas."
        lista_de_tarefas = []
        for i, tarefa in enumerate(self._tarefas, start=1):
            lista_de_tarefas.append(f'Tarefa nº{i}: {tarefa._tarefa}')
        return "\n" + "\n".join(lista_de_tarefas)



