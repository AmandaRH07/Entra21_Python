#--- Exercício 2  - Funções
#--- Escreva uma função para cadastro de endereço:
#---       a função deve receber sete parâmetros, id da pessoa, rua, numero, complemento, bairro, cidade e estado
#---       a função deve salvar os dados de endereço em uma lista com escopo global
#---       a função deve permitir o cadastro apenas de endereços com todos os dados preenchidos
#---       a função deve retornar uma mensagem ao final de acordo com a situação
#--- A função deve ser salva em um arquivo diferente do arquivo principal onde será chamada

from Ex1 import cadastroPessoa

enderecos = []
def cadastroEndereco(rua, numero, comp, bairro, cidade, estado):
    endereco = {}
    endereco['rua'] = rua
    if (not rua):
        return "Campo 'Rua' vazio! Não é possível cadastrar."
    endereco['numero'] = numero
    if (not numero):
        return "Campo 'Número' vazio! Não é possível cadastrar."
    endereco['complemento'] = comp
    if (not comp):
        return "Campo 'Complemento' vazio! Não é possível cadastrar."
    endereco['bairro'] = bairro
    if (not bairro):
        return "Campo 'Bairro' vazio! Não é possível cadastrar."
    endereco['cidade'] = cidade
    if (not cidade):
        return "Campo 'Cidade' vazio! Não é possível cadastrar."
    endereco['estado'] = estado
    if (not estado):
        return "Campo 'Estado' vazio! Não é possível cadastrar."
    enderecos.append(endereco)
    return "Endereço cadastrado com sucesso!"

def mostrarDadosDeEndereco():
    for i in enderecos:
        print(i)
        print(f"RUA: {i['rua']}")
        print(f"NUMERO: {i['numero']}")
        print(f"COMPLEMENTO: {i['complemento']}")
        print(f"BAIRRO: {i['bairro']}")
        print(f"CIDADE: {i['cidade']}")
        print(f"ESTADO: {i['estado']}")
