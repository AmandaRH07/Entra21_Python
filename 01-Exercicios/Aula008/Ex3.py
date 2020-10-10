#--- Exercício 3  - Funções
#--- Escreva uma função para listar pessoas cadastradas:
#---    a função deve retornar todas as pessoas cadastradas na função do ex1
#--- Escreva uma função para exibir uma pessoa específica:
#        a função deve retornar uma pessoa cadastrada na função do ex1 filtrando por id

from Ex1 import cadastroPessoa

def listarPessoas():
    cadastroPessoa()
    return f"""Id: {idPessoa}
    Nome: {Nome}
    Sobrenome: {Sobrenome}
    Idade: {Idade}"""

def pessoaEspecifica(id):
    if id == IdPessoa:
        return 'entrou no pessoa especifica'
        #listarPessoas()
