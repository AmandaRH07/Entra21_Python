#--- Exercício 5  - Funções
#--- Escreva um programa para cadastro de pessoas e endereços:
#---       o programa deve solicitar os dados de pessoa utilizados na função do ex1
#---       o programa deve solicitar os dados de endereços utilizados na função do ex2
#---       o programa deve passar o id obtido na função do ex1 para a função do ex2
#---       o programa deve mostrar ao final os dados de todos as pessoas cadastradas 
#                com seus respectivos endereços utilizando as funções do ex3 e ex4

from Ex1 import cadastroPessoa, mostrarDadosPessoais, pessoaEspecifica
from Ex2 import cadastroEndereco, mostrarDadosDeEndereco, pesquisaEndereco

def cabecalho(tipo_de_cadastro):
    print("\n**    CADASTRO DE {}     **".format(tipo_de_cadastro))  

def menu():
    opcao = ''
    while opcao != 4:
        opcao = int(input("""
        Cadastramento
        \t 1. Cadastrar uma nova pessoa
        \t 2. Busca dados pessoais por ID
        \t 3. Buscar endereço por ID
        \t 4. Listar e sair
        Insira a opção escolhida: """)) 
        if opcao == 1:
            cabecalho("PESSOA")
            nome = input("Nome: ")
            sobrenome = input("Sobrenome: ")
            idade = int(input("Idade: "))
            if idade < 18:
                print("Cadastro negado, menor de 18 anos")
                pass
            else: 
                cadastroPessoa(nome,sobrenome,idade)

                cabecalho("ENDEREÇO")
                rua = input("Rua: ")
                '''if rua.isspace():
                    while rua.isspace():
                        rua = input("Rua não cadastrada, tente novamente! Rua: ")'''             
                numero = input("Número: ")
                complemento = input("Complemento: ")
                bairro = input("Bairro: ")
                cidade = input("Cidade: ")
                estado = input("Estado: ")
                cadastroEndereco(rua,numero,complemento,bairro,cidade,estado)
        elif opcao == 2:
            pessoaEspecifica()
        elif opcao == 3:
            pesquisaEndereco()
        elif opcao == 4:
            print("\nDADOS: ")
            cabecalho("PESSOA")
            mostrarDadosPessoais()
            cabecalho("ENDEREÇO")
            mostrarDadosDeEndereco()
        else:
            pass
menu()