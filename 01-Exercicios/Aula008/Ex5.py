#--- Exercício 5  - Funções
#--- Escreva um programa para cadastro de pessoas e endereços:
#---       o programa deve solicitar os dados de pessoa utilizados na função do ex1
#---       o programa deve solicitar os dados de endereços utilizados na função do ex2
#---       o programa deve passar o id obtido na função do ex1 para a função do ex2
#---       o programa deve mostrar ao final os dados de todos as pessoas cadastradas 
#                com seus respectivos endereços utilizando as funções do ex3 e ex4

from Ex1 import cadastro_Pessoa, mostrar_Dados, pesquisa_Pessoa
from Ex2 import cadastro_Endereco, mostrar_Endereco, pesquisa_Endereco
caracter = "_"

#Definição de funções para cabeçalhos;
def cabecalho(tipo_de_cadastro):
    print(caracter * 48)
    print("               CADASTRO DE {}              ".format(tipo_de_cadastro))
    print(caracter * 48)

def pesquisa(pesquisa):
    print(caracter * 48)
    print("               PESQUISA DE {}              ".format(pesquisa))
    print(caracter * 48)

def lista():
    print(caracter * 48)
    print("               LISTA DE CADASTROS             ")
    print(caracter * 48)

def opcoes():
    print(caracter * 48)
    print("**                MENU DE OPÇÕES              **")
    print(caracter * 48)

#Desenvolvimento do menu principal e entradas do algoritmo;
def menu():
    opcao = ''
    while (opcao != 4):
        opcoes()
        opcao = int(input("""
        
    \t 1. Cadastrar uma nova pessoa
    \t 2. Busca dados pessoais por ID
    \t 3. Buscar endereço por ID
    \t 4. Listar e sair
        Insira a opção escolhida: """))
        
        """
        if (opcao < 1 or opcao > 4):
            opcao = input("Entrada inválida! Digite novamente: ")
        else:"""

        if (opcao == 1):
            cabecalho("PESSOA")

            nome = input("Nome: ")
            while(not nome):
                nome = input("Campo 'Nome' vazio!\nNome: ")

            sobrenome = input("Sobrenome: ")
            while(not sobrenome):
                sobrenome = input("Campo 'Sobrenome' vazio!\nSobrenome: ")
                
            idade = int(input("Idade: "))
            while(not idade):
                idade = input("Campo 'Idade' vazio!\nIdade: ")

            if (idade < 18):
                print("Cadastro negado, menor de 18 anos")
            else: 
                cadastro_Pessoa(nome,sobrenome,idade)
                cabecalho("ENDEREÇO")

                rua = input("Rua: ")
                while(not rua):
                    rua = input("Campo 'Rua' vazio!\nRua: ")

                numero = input("Número: ")
                while(not numero):
                    numero = input("Campo 'Número' vazio\nNúmero: ")

                comp = input("Complemento: ")
                while(not comp):
                    comp = input("Campo 'Complemento' vazio!Complemento: ")

                bairro = input("Bairro: ")
                while(not bairro):
                    bairro = input("Campo 'Bairro' vazio!\nBairro: ")
                
                cidade = input("Cidade: ")
                while(not cidade):
                    cidade = input("Campo 'Cidade' vazio\nCidade: ")

                estado = input("Estado: ")
                while(not estado):
                    estado = input("Campo 'Estado' vazio!\nCidade: ")
                cadastro_Endereco(rua,numero,comp,bairro,cidade,estado)

        elif (opcao == 2):
            pesquisa("ID")
            pesquisa_Pessoa()

        elif (opcao == 3):
            pesquisa("ENDEREÇO")
            pesquisa_Endereco()
            
        elif (opcao == 4):
            lista()
            print("\nDADOS: ")
            mostrar_Dados()
            mostrar_Dados()
menu()