#--- Exercício 1  - Funções
#--- Escreva uma função para cadastro de pessoa:
#---       a função deve receber três parâmetros, nome, sobrenome e idade
#---       a função deve salvar os dados da pessoa em uma lista com escopo global
#---       a função deve permitir o cadastro apenas de pessoas com idade igual ou superior a 18 anos
#---       a função deve retornar uma mensagem caso a idade informada seja menor que 18
#---       caso a pessoa tenha sido cadastrada com sucesso deve ser retornado um id 
#--- A função deve ser salva em um arquivo diferente do arquivo principal onde será chamada

# pessoa = {"id": id, "nome": nome, "sobrenome" : sobrenome}}
# pessoas = [pessoa1, pessoa2]

pessoas = []
def cadastroPessoa(idPessoa, nome, sobrenome, idade):
    pessoa = {"idPessoa": idPessoa}
    pessoa['nome'] = nome
    pessoa['sobrenome'] = sobrenome
    pessoa['idade'] = idade
    for i in pessoas: 
        pessoa['idPessoa'] = idPessoa + 1
    pessoas.append(pessoa)
        
def mostrarDadosPessoais():
    for i in pessoas:
        print(i)
        print(f"ID: {i['idPessoa']}")
        print(f"NOME: {i['nome']}")
        print(f"SOBRENOME: {i['sobrenome']}")
        print(f"IDADE: {i['idade']}")
        
      