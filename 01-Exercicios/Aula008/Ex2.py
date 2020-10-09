#--- Exercício 2  - Funções
#--- Escreva uma função para cadastro de endereço:
#---       a função deve receber sete parâmetros, id da pessoa, rua, numero, complemento, bairro, cidade e estado
#---       a função deve salvar os dados de endereço em uma lista com escopo global
#---       a função deve permitir o cadastro apenas de endereços com todos os dados preenchidos
#---       a função deve retornar uma mensagem ao final de acordo com a situação
#--- A função deve ser salva em um arquivo diferente do arquivo principal onde será chamada

'''
#Função de cadastro;
def cadastroEndereco(idPessoa, endereco) -> str:
    cadastrado = [idPessoa, endereco]
    #CADASTRO apenas se todos os dados preenchidos
    return "Endereço cadastrado com sucesso!"

#Variável Global;
endereco = [rua, numero, comp, bairro, cidade, estado]

#Chamada da função;
enderecoCadastrado = cadastroEndereco(endereco)'''


def cadastroEndereco(rua, numero, comp, bairro, cidade, estado):
    dados_cadastrados_endereco = [rua, numero, comp, bairro, cidade, estado]
    return "Endereço cadastrado com sucesso!"

def id_Endereco(idPessoa, endereco) -> str:
    cadastrado = [idPessoa, endereco]
    #CADASTRO apenas se todos os dados preenchidos
    return "Endereço cadastrado com sucesso!"