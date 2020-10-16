#--- Exercício 2  - Funções
#--- Escreva uma função para cadastro de endereço:
#---       a função deve receber sete parâmetros, id da pessoa, rua, numero, complemento, bairro, cidade e estado
#---       a função deve salvar os dados de endereço em uma lista com escopo global
#---       a função deve permitir o cadastro apenas de endereços com todos os dados preenchidos
#---       a função deve retornar uma mensagem ao final de acordo com a situação
#--- A função deve ser salva em um arquivo diferente do arquivo principal onde será chamada
#--- Exercício 4  - Funções
#--- Escreva uma função para listar endereços cadastrados:
#---    a função deve retornar todos os endereços cadastrados na função do ex2
#--- Escreva uma função para exibir um endereço específico:
#        a função deve retornar um endereço cadastrado na função do ex2 filtrando por 
#            id da pessoa

from Ex1 import cadastro_Pessoa

enderecos = []
endereco = {}
id_pessoa = 0
id_igual = False

def cadastro_Endereco(rua, numero, comp, bairro, cidade, estado):
    global id_pessoa
    id_pessoa += 1
    endereco = {"id_pessoa": id_pessoa}
    endereco['rua'] = rua
    endereco['numero'] = numero
    endereco['comp'] = comp
    endereco['bairro'] = bairro
    endereco['cidade'] = cidade
    endereco['estado'] = estado
    enderecos.append(endereco)
    return id_pessoa

def mostrar_Endereco():
    for i in enderecos:
        print(f"ID: {i['id_pessoa']}")
        print(f"Rua: {i['rua']}")
        print(f"Número: {i['numero']}")
        print(f"Complemento: {i['comp']}")
        print(f"Bairro: {i['bairro']}")
        print(f"Cidade: {i['cidade']}")
        print(f"Estado: {i['estado']}")

def pesquisa_Endereco():
    endereco_especifico = int(input("Insira o ID do endereço a ser pesquisado: "))
    
    if id_pessoa == endereco_especifico:
        mostrar_Endereco()
    else:
        print("Id não encontrado")
    
    arquivoDados = open("cadastro.txt", 'r')
    for linha in arquivoDados:
        lista_dados = linha.split(',')
        if id_pessoa == endereco_especifico:
            print(f""""Dados do Arquivo:
            ID: {lista_dados[0]}
            Rua: {lista_dados[1]}
            Numero: {lista_dados[2]}
            Complemento: {lista_dados[3]}
            Bairro: {lista_dados[4]}
            Cidade: {lista_dados[5]}
            Estado: {lista_dados[6]}""")
    arquivoDados.close()
