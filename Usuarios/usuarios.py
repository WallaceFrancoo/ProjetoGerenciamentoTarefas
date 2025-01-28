class Usuarios:
    usuarios = []

    def __init__(self,nome, departamento, senha):
        self._nome = nome
        self._departamento = departamento
        self._senha = senha
        Usuarios.usuarios.append(self)

    def __str__(self):
        return self._nome

    @classmethod
    def mostrar_usuarios(cls):
        for usuario in cls.usuarios:
            print(f'{usuario._nome} é do departamento {usuario.departamento} a senha dele é: {usuario._senha}')

    @property
    def departamento(self):
        print(self._departamento)
        return 'Departamento de Tecnologia' if self._departamento == 'T.I' else 'Cadastrar departamento'

usuario_wallace = Usuarios('Wallace','T.I','1188')
usuario_daniel = Usuarios('Daniel','T.I','1188')
Usuarios.mostrar_usuarios()