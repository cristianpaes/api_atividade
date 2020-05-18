from models import Pessoas, Usuarios

# Insere dados na tabela
def insere_pessoas():
    pessoa = Pessoas(nome='Felipe', idade=22)
    print(pessoa)
    pessoa.save()

# Consulta dados na tabela
def consulta_pessoas():
    pessoa = Pessoas.query.all()
    print(pessoa)
    pessoa = Pessoas.query.filter_by(nome='Cristian').first()
    print(pessoa.idade)

# Altera dados na tabela
def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Cristian').first()
    pessoa.idade = 21
    pessoa.save()

# Exclui dados na tabela
def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Felipe').first()
    pessoa.delete()

# Insere dados na tabela Usuarios
def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()

# Consulta dados na tabela Usuarios
def consulta_todos_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)

if __name__ == '__main__':
    #insere_pessoas()
    #altera_pessoa()
    #exclui_pessoa()
    #consulta_pessoas()
    insere_usuario('Cristian', '123')
    insere_usuario('Rafael', '4321')
    consulta_todos_usuarios()
