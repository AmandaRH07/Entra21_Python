#--- Exercício 5  - Funções
#--- Escreva um programa para cadastro de pessoas e endereços:
#---       o programa deve solicitar os dados de pessoa utilizados na função do ex1
#---       o programa deve solicitar os dados de endereços utilizados na função do ex2
#---       o programa deve passar o id obtido na função do ex1 para a função do ex2
#---       o programa deve mostrar ao final os dados de todos as pessoas cadastradas 
#                com seus respectivos endereços utilizando as funções do ex3 e ex4

from Ex1 import cadastroPessoa
from Ex2 import cadastroEndereco
from Ex3 import listarPesso

def cabecalho(tipo_de_cadastro):
    print("\n**    CADASTRO DE {}     **".format(tipo_de_cadastro))

cabecalho("PESSOA")
nome = input("Nome: ")
sobrenome = input("Sobrenome: ")
idade = int(input("Idade: "))
cadastroPessoa(nome,sobrenome,idade)

cabecalho("ENDEREÇO")
rua = input("Rua: ")
numero = input("Número: ")
complemento = input("Complemento: ")
bairro = input("Bairro: ")
cidade = input("Cidade: ")
estado = input("Estado: ")
cadastroEndereco(rua,numero,complemento,bairro,cidade,estado)



