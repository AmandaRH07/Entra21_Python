#--- Exercício 4  - Funções
#--- Escreva uma função para listar endereços cadastrados:
#---    a função deve retornar todos os endereços cadastrados na função do ex2
#--- Escreva uma função para exibir um endereço específico:
#        a função deve retornar um endereço cadastrado na função do ex2 filtrando por 
#            id da pessoa

from Ex2 import cadastroEndereco

def listarEnderecos():
    mostrarDadosDeEndereco()

def pesquisaEndereco(idPessoa):
    #Chama função de endereço;
    for i in range(len(enderecos)):
        endereco = enderecos[i]
        if (idPessoa == endereco.get("ID")):
            return endereco