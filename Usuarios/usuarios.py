class Usuarios:
    def __init__(self,nome, departamento, senha):
        self.nome = nome
        self.departamento = departamento
        self.senha = senha


usuario_wallace = Usuarios('Wallace','T.I','1188')
usuario_daniel = Usuarios('Daniel','T.I','1188')
print(vars(usuario_wallace))
print(vars(usuario_daniel))