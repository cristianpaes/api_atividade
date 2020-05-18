from models import Pessoas

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

if __name__ == '__main__':
    #insere_pessoas()
    #altera_pessoa()
    exclui_pessoa()
    consulta_pessoas()
