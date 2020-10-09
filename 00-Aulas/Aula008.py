# Dicionários e Funções - Parte 2

#== Dicionários
# Conjunto de dados, chave e não indice
animal1 = {'grupo': 'ave',
'alimentação':'carnívoro', 
'especie' : 'urubu',
'habitat':'Mata Atlantica',
'voa': True }
animal2 = {'grupo': 'mamifero',
'alimentação':'onivoro',
'especie' :'ornintorrinco', 
'habitat':'Australia',
'voa': True }
'''
animal3 = {}
animal3['grupo'] = input()
animal3['alimentação'] = input()
animal3['especie'] = input()
animal3['habitat'] = input()
animal3['voa'] = input()'''

#== escopo global
animais = [animal1, animal2]


#== Função
# Typehinting "->"str = quando for executada, a função vai retornar um str
def funcao_cadastrar_animal(grupo:str, alimentacao:str, especie:str, habitat:str, voa:bool) ->str:
    #== escopo local ou de função
    animal = {}
    animal['grupo'] = grupo
    animal['alimentação'] = alimentacao
    animal['especie'] = especie
    animal['habitat'] = habitat
    animal['voa'] = voa
    animais.append(animal)
    return "animal cadastrado com sucesso"

funcao_cadastrar_animal('ave','herbivoro', 'dinossauro', 'deserto',True)

for a in animais:
    print(a['especie'])

#== Procedimento
# não tem return, executa um conjunto de instruções

def procedimento_cadastrar_animal(grupo, alimentacao, especie, habitat, voa):
    #== escopo local ou de função
    animal = {}
    animal['grupo'] = grupo
    animal['alimentação'] = alimentacao
    animal['especie'] = especie
    animal['habitat'] = habitat
    animal['voa'] = voa
    animais.append(animal)
    