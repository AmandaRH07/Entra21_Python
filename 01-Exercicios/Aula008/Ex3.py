#--- Exercício 3  - Funções
#--- Escreva uma função para listar pessoas cadastradas:
#---    a função deve retornar todas as pessoas cadastradas na função do ex1
#--- Escreva uma função para exibi uma pessoa específica:
#        a função deve retornar uma pessoa cadastrada na função do ex1 filtrando por id

from Ex1 import cadastroPessoa

def listar_pessoas():
    cadastro_pessoa()
    return f"""Id: {idPessoa}
    Nome: {Nome}
    Sobrenome: {Sobrenome}
    Idade: {Idade}"""