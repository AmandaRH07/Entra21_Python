#--- Exercício 3  - Funções
#--- Escreva uma função para listar pessoas cadastradas:
#---    a função deve retornar todas as pessoas cadastradas na função do ex1
#--- Escreva uma função para exibir uma pessoa específica:
#        a função deve retornar uma pessoa cadastrada na função do ex1 filtrando por id

from Ex1 import cadastroPessoa

def listarPessoas():
    mostrarDadosPessoais()

def pessoaEspecifica(idPessoa):
    '''print(f"EX3: idpessoa {idPessoa}")
    idEspecifico = input("Insira o ID a ser pesquisado: ")
    print(f"EX3: id especifico {idEspecifico}")
    if idEspecifico == idPessoa:
        print('entrou no pessoa especifica') 
        listarPessoas()'''
    for i in range(len(pessoas)):
        pessoa = pessoas[i]
        if (idPessoa == pessoa.get("ID")):
            return pessoa
